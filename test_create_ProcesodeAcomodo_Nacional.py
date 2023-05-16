# TERMINADO
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
    def test_PurchaseOrder_ProcesodeAcomodo_Nacional(self):
        """TC7 ESTE TEST CASE NECESITA FACTURAS CON STATUS  'RECIBIDA EN PROCESO DE REVISION' """
        #print("Test using: "+supplier)
        sge_funct = sge_functions2()
        print("------------------------------Test to Create Purchase Order Proceso de Acomodo Nacional")
        print("1	Ingresar a SGE con las credenciales <<User>> <Password>>")
        sge_funct.login_adm_sge(login_data.adm_username, login_data.ip, login_data.adm_password)
        conectado = sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial)
        if conectado:
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
            print("10	Seleccionar <<OPCION MENU>>	2")
            sge_funct.send_text("2")
            print("11   Situarse en la orden de compra e ingresar el numero de PO.	pegar_num_po_transito")
            num_factura_en_proceso_de_revision, inv_factura_en_proceso_de_revision, nombre_archivo = sge_funct.obtener_factura_de_directorio(files.inv_recibida_en_revision_folder)
            "obtener_factura_en_proceso_de_revision"
            # se envia el numero de po
            print(f"pegando {num_factura_en_proceso_de_revision}")
            sge_funct.send_text(num_factura_en_proceso_de_revision)
            print("15	Teclear input 	Enter")
            sge_funct.press_enter()
            print("16	Teclear input 	s")
            sge_funct.send_text("s")
            print("17	Teclear input 	Enter")
            sge_funct.press_enter()
            print("18	Situarse en la secuencia 001 con el input	flecha_abajo")
            sge_funct.press_hotkeys("ctrl+down")
            print("19   Presionar la combinacion de teclas: Ctrl + k")
            sge_funct.press_hotkeys("ctrl+k")
            print("20	Ingresar en Login del <<UsuarioAlmacen>>	pendiente")
            sge_funct.send_text("jmartin")
            print("21	Teclear input 	Enter")
            sge_funct.press_enter()
            print("22	Ingresar en Login del <<PassAlmacen>>	pendiente")
            sge_funct.send_text("123")
            print("23	Teclear input 	Enter")
            sge_funct.press_enter()
            # posible delay para siguiente pantalla
            sge_funct.segundos_de_espera(2)
            print("24   Presionar la combinacion de teclas: Ctrl + a")
            sge_funct.press_hotkeys('ctrl+a')
            print("25   Presionar la combinacion de teclas: Ctrl + k")
            sge_funct.press_hotkeys('ctrl+k')
            print("26	Ingresar en Login del <<UsuarioAlmacen>>	pendiente")
            sge_funct.send_text("jmartin")
            print("27	Teclear input 	Enter")
            sge_funct.press_enter()
            print("28	Ingresar en Login del <<PassAlmacen>>	pendiente")
            sge_funct.send_text("123")
            print("29	Teclear input 	Enter")
            sge_funct.press_enter()
            print("Validating Purchase Order Status...")
            img_status = images.img_status_en_proceso_de_acomodo
            nombre_status = "STATUS EN PROCESO DE ACOMODO"
            if sge_funct.validar_po_status2(img_status, nombre_status):
                print(f"Status {nombre_status} validado correctamente")
                print("moviendo factura '/recibido_en_revision' a '/en_proceso_de_acomodo'")
                sge_funct.mover_factura_status_recibida_en_proceso_de_revision_a_proceso_Acomodo_Nacional(num_factura_en_proceso_de_revision)
            else:
                print("Fallo validacion, estatus Incorrecto")
                assert False, "Fallo validacion, estatus Incorrecto"

        else:
            print(conectado)
            assert conectado, "error de conexion"


    def tearDown(self):
        sge_funct = sge_functions2()
        #sge_funct.terminate_sge_session()


if __name__ == '__main__':
    unittest.main()
