import unittest

from app import create_app


class PruebaBasica(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_pagina_inicio_responde(self):
        respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn("Sprint 0".encode(), respuesta.data)


if __name__ == "__main__":
    unittest.main()
