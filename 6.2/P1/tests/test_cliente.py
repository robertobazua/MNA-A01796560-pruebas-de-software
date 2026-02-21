"""
Módulo test_cliente.py
Contiene las pruebas unitarias para la clase Cliente.
Usa una base de datos temporal para no afectar produccion.
"""

import unittest
import os
from source.cliente import Cliente
import source.cliente

# Archivo temporal para pruebas
ARCHIVO_PRUEBAS = "bd_clientes_pruebas.csv"
COLUMNAS = ["id_cliente", "nombre", "email"]


class TestCliente(unittest.TestCase):
    """Pruebas unitarias para la clase Cliente"""

    def setUp(self):
        """Limpia el entorno antes de cada prueba individual."""
        self.archivo_test = ARCHIVO_PRUEBAS
        source.cliente.ARCHIVO = self.archivo_test

        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)

    def tearDown(self):
        """Limpia el entorno de pruebas después de cada test"""
        if os.path.exists(ARCHIVO_PRUEBAS):
            os.remove(ARCHIVO_PRUEBAS)

    def test_crear_cliente_exitoso(self):
        """Test para crear un cliente exitosamente"""
        resultado = Cliente.crear_cliente("C001", "Roberto Bazua",
                                          "roberto.bazua@tec.mx")
        self.assertTrue(resultado)

    def test_crear_cliente_duplicado(self):
        """Test para crear un cliente con ID duplicado"""
        Cliente.crear_cliente("C001", "Roberto Bazua", "roberto.bazua@tec.mx")
        resultado = Cliente.crear_cliente("C001", "Otro Cliente",
                                          "otro@ejemplo.com")
        self.assertFalse(resultado)

    def test_eliminar_cliente_exitoso(self):
        """Test para eliminar un cliente exitosamente"""
        Cliente.crear_cliente("C002", "Maria Lopez", "maria.lopez@tec.mx")
        resultado = Cliente.eliminar_cliente("C002")
        self.assertTrue(resultado)

    def test_eliminar_cliente_no_existente(self):
        """Test para eliminar un cliente que no existe"""
        resultado = Cliente.eliminar_cliente("C999")
        self.assertFalse(resultado)

    def test_listar_clientes_vacio(self):
        """Test para listar clientes cuando no hay registros"""
        resultado = Cliente.listar_clientes()
        self.assertTrue(resultado.empty)

    def test_listar_clientes_con_registros(self):
        """Test para listar clientes cuando hay registros"""
        Cliente.crear_cliente("C003", "Ana Gomez", "ana.gomez@tec.mx")
        resultado = Cliente.listar_clientes()
        self.assertTrue(len(resultado) > 0)
