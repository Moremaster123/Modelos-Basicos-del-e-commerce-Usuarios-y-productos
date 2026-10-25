from django.contrib.auth.models import User
from django.test import TestCase

from .models import PerfilUsuario, Producto


class ModelosTests(TestCase):
    fixtures = ['productos']

    def test_productos_cargados(self):
        self.assertEqual(Producto.objects.count(), 20)
        self.assertEqual(str(Producto.objects.get(pk=1)), 'Tinta Negra')
        self.assertEqual(Producto.objects.filter(categoria='Anime y manga').count(), 7)

    def test_perfil_de_usuario(self):
        usuario = User.objects.create_user('ana', 'ana@correo.com', 'ClaveAna2026')
        perfil = PerfilUsuario.objects.create(usuario=usuario, direccion='Calle 1', telefono='5512345678')
        self.assertEqual(str(perfil), 'ana')
        self.assertEqual(usuario.perfilusuario, perfil)

    def test_admin(self):
        admin = User.objects.create_superuser('admin', 'admin@correo.com', 'ClaveAdmin2026')
        self.client.force_login(admin)
        for url in ['/admin/ecommerce/producto/', '/admin/ecommerce/producto/1/change/',
                    '/admin/ecommerce/perfilusuario/', '/admin/ecommerce/perfilusuario/add/']:
            self.assertEqual(self.client.get(url).status_code, 200, url)
