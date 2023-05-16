# TERMIANDO
import unittest
from Config.config import login_data, images, csv_files_path, files
from sge_functions.sge_functions2 import sge_functions2
from Config.config import csv_files_path
from Config.config import txt_files_path
import pyautogui as pa
from ddt import ddt, file_data


#@ddt
class SgePoUnittest(unittest.TestCase):

    #@file_data("./Config/TestDataset/dataSet_ddt_po.json")
    def test_PurchaseOrder_AcomodadoPendienteEntrada_Nacional(self):
        """TC_8 ESTE TEST CASE NECESITA FACTURAS CON STATUS  'RECIBIDA EN PROCESO DE ACOMODO' """
        #print("Test using: "+supplier)
        sge_funct = sge_functions2()
        print("------------------------------Test to Create Purchase Order Acomodado Pendiente Entrada Nacional")
        print("1	Ingresar a SGE con las credenciales <<User>> <Password>>")
        sge_funct.login_adm_sge(login_data.adm_username, login_data.ip, login_data.adm_password)
        conectado = sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial)
        if conectado:
            print("1.1   cambiar usuario con permisos Teclando input  uu")
            sge_funct.send_text("uu")
            sge_funct.segundos_de_espera(1)
            sge_funct.send_text("jmartin")
            print("1.2	Teclear input 	Enter")
            sge_funct.press_enter()
            print("2	Seleccionar <<Sucursal>>	12")
            sge_funct.send_text("12")
            print("3	Teclear input 	Enter")
            sge_funct.press_enter()
            print("4	Seleccionar <<OPCION MENU>>	2")
            sge_funct.send_text("2")
            print("5	Teclear input 	Enter")
            sge_funct.press_enter()
            print("6	Seleccionar <<OPCION MENU>>	4")
            sge_funct.send_text("4")
            print("7	Teclear input 	Enter")
            sge_funct.press_enter()
            print("8	Seleccionar <<OPCION MENU>>	10")
            sge_funct.send_text("10")
            print("9	Teclear input 	Enter")
            sge_funct.press_enter()
            print("10	Seleccionar <<OPCION MENU>>	7")
            sge_funct.send_text("7")
            print("11	Ingresar el proveedor configurado 'TENNECO'")
            sge_funct.send_text("TENNECO")
            print("12	Teclear input 	Enter")
            sge_funct.press_enter()
            print("13  Buscar Factura configurada y pegarla")
            directorio_origen = files.inv_en_proceso_de_acomodo_folder
            num_factura_recibida_en_proceso_de_acomodo, inv_factura_recibida_en_proceso_de_acomodo, nombre_archivo = sge_funct.obtener_factura_de_directorio(directorio_origen)
            # se envia el inv de po
            print(f"pegando {inv_factura_recibida_en_proceso_de_acomodo}")
            sge_funct.send_text(inv_factura_recibida_en_proceso_de_acomodo)
            sge_funct.segundos_de_espera(1)
            print("14   Presionar la combinacion de teclas: Ctrl + f")
            sge_funct.press_hotkeys("ctrl+f")
            print("15	Ingresar en Login del <<UsuarioAlmacen>>	pendiente")
            sge_funct.send_text("jmartin")
            print("16	Teclear input 	Enter")
            sge_funct.press_enter()
            print("Validating Purchase Order Status...")
            img_status = images.img_status_en_proceso_de_acomodo
            nombre_status_esperado = "STATUS ACOMODADA PEND ENT T"
            if sge_funct.validar_po_status2(img_status, nombre_status_esperado):
                print(f"Status {nombre_status_esperado} validado correctamente")
                print("moviendo factura '/en_proceso_de_acomodo' a '/acomodado_pendiente_de_entrada'")
                directorio_origen = files.inv_en_proceso_de_acomodo_folder
                directorio_destino = files.inv_acomodado_pendiente_de_entrada_folder
                sge_funct.mover_facturas(num_factura_recibida_en_proceso_de_acomodo, directorio_origen, directorio_destino)
            else:
                print("Fallo validacion, estatus Incorrecto")
                assert False, "Fallo validacion, estatus Incorrecto"

        else:
            print(conectado)
            assert conectado, "error de conexion"


    def tearDown(self):
        sge_funct = sge_functions2()
        sge_funct.terminate_sge_session()


if __name__ == '__main__':
    unittest.main()
