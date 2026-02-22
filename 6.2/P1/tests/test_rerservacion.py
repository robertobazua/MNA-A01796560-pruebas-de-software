"""
Módulo test_reservacion.py
Contiene las pruebas unitarias para la clase Reservacion.
Usa una base de datos temporal para no afectar produccion.
"""

import unittest
import os
import source.reservacion
import source.cliente
import source.hotel
from source.reservacion import Reservacion
from source.cliente import Cliente
from source.hotel import Hotel

# Archivos temporales para pruebas
RES_FILE = "temp_res.csv"
CLI_FILE = "temp_cli_res.csv"
HOT_FILE = "temp_hot_res.csv"


class TestReservacion(unittest.TestCase):
    """Pruebas unitarias para la reservacion de Hotel"""

    def setUp(self):
        """Limpia el entorno antes de cada prueba individual."""
        source.reservacion.ARCHIVO = RES_FILE
        source.cliente.ARCHIVO = CLI_FILE
        source.hotel.ARCHIVO = HOT_FILE

        for archivo in [RES_FILE, CLI_FILE, HOT_FILE]:
            if os.path.exists(archivo):
                os.remove(archivo)

        # Crear clientes y hoteles de prueba
        Cliente.crear_cliente("C001", "Roberto Bazua",
                              "roberto.bazua@tec.mx")
        Hotel.crear_hotel("H001", "Hotel 1", "Calle 123", 50)

    def tearDown(self):
        """Limpia el entorno de pruebas luego de cada test"""
        for archivo in [RES_FILE, CLI_FILE, HOT_FILE]:
            if os.path.exists(archivo):
                os.remove(archivo)

    def test_crear_reservacion_exitoso(self):
        """Test para crear una reservacion exitosamente"""
        resultado = Reservacion.crear_reservacion("R001", "C001", "H001", 3)
        self.assertTrue(resultado)

    def test_crear_reservacion_cliente_no_existente(self):
        """Test para crear una reservacion con cliente no existente"""
        resultado = Reservacion.crear_reservacion("R001", "C002", "H001", 3)
        self.assertFalse(resultado)

    def test_crear_reservacion_hotel_no_existente(self):
        """Test para crear una reservacion con hotel no existente"""
        resultado = Reservacion.crear_reservacion("R001", "C001", "H002", 3)
        self.assertFalse(resultado)

    def test_cancelar_reservacion_exitoso(self):
        """Test para cancelar una reservacion exitosamente"""
        Reservacion.crear_reservacion("R001", "C001", "H001", 3)
        resultado = Reservacion.cancelar_reservacion("R001")
        self.assertTrue(resultado)

    def test_cancelar_reservacion_no_existente(self):
        """Test para cancelar una reservacion no existente"""
        resultado = Reservacion.cancelar_reservacion("R001")
        self.assertFalse(resultado)

    def test_listar_reservaciones(self):
        """Test para listar todas las reservaciones"""
        Reservacion.crear_reservacion("R001", "C001", "H001", 3)
        Reservacion.crear_reservacion("R002", "C001", "H001", 3)
        resultado = Reservacion.listar_reservaciones()
        self.assertEqual(len(resultado), 2)
