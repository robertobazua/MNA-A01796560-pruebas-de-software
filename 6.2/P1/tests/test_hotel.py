"""
Módulo test_hotel.py
Contiene las pruebas unitarias para la clase Hotel.
Usa una base de datos temporal para no afectar produccion.
"""

import unittest
import os
from source.hotel import Hotel
import source.hotel

ARCHIVO_PRUEBAS = "bd_hoteles_pruebas.csv"


class TestHotel(unittest.TestCase):
    """Pruebas unitarias para la clase Hotel"""
    def setUp(self):
        self.archivo_test = ARCHIVO_PRUEBAS
        source.hotel.ARCHIVO = self.archivo_test

        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)

    def tearDown(self):
        """Limpia el entorno de pruebas después de cada test"""
        if os.path.exists(ARCHIVO_PRUEBAS):
            os.remove(ARCHIVO_PRUEBAS)

    def test_crear_hotel_exitoso(self):
        """Test para crear un hotel exitosamente"""
        id_hotel = "H001"
        nombre = "Hotel 1"
        direccion = "Calle 123"
        disponibilidad = 50
        resultado = Hotel.crear_hotel(id_hotel, nombre, direccion,
                                      disponibilidad)
        self.assertTrue(resultado)

    def test_crear_hotel_duplicado(self):
        """Test para crear un hotel con ID duplicado"""
        id_hotel = "H001"
        nombre = "Hotel 1"
        direccion = "Calle 123"
        disponibilidad = 50
        Hotel.crear_hotel(id_hotel, nombre, direccion, disponibilidad)
        resultado = Hotel.crear_hotel(id_hotel, "Hotel 2", "Calle 456", 100)
        self.assertFalse(resultado)

    def test_eliminar_hotel_exitoso(self):
        """Test para eliminar un hotel exitosamente"""
        id_hotel = "H001"
        Hotel.crear_hotel(id_hotel, "Hotel 1", "Calle 123", 50)
        resultado = Hotel.eliminar_hotel(id_hotel)
        self.assertTrue(resultado)

    def test_eliminar_hotel_no_existente(self):
        """Test para eliminar un hotel que no existe"""
        id_hotel = "H999"
        resultado = Hotel.eliminar_hotel(id_hotel)
        self.assertFalse(resultado)

    def test_modificar_hotel_exitoso(self):
        """Test para modificar un hotel exitosamente"""
        id_hotel = "H001"
        Hotel.crear_hotel(id_hotel, "Hotel 1", "Calle 123", 50)
        resultado = Hotel.modificar_hotel(id_hotel, nombre="Hotel 2",
                                          direccion="Calle 456",
                                          disponibilidad=100)
        self.assertTrue(resultado)

    def test_modificar_hotel_no_existente(self):
        """Test para modificar un hotel que no existe"""
        id_hotel = "H999"
        resultado = Hotel.modificar_hotel(id_hotel, nombre="Hotel 2",
                                          direccion="Calle 456",
                                          disponibilidad=100)
        self.assertFalse(resultado)

    def test_listar_hoteles(self):
        """Test para listar todos los hoteles"""
        Hotel.crear_hotel("H001", "Hotel 1", "Calle 123", 50)
        Hotel.crear_hotel("H002", "Hotel 2", "Calle 456", 100)
        resultado = Hotel.listar_hoteles()
        self.assertEqual(len(resultado), 2)

    def test_listar_hoteles_vacio(self):
        """Test para listar todos los hoteles cuando no hay registros"""
        resultado = Hotel.listar_hoteles()
        self.assertEqual(len(resultado), 0)
