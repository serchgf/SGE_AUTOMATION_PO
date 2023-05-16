# terminado
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
    def test_PurchaseOrder_PurchaseOrder_RecibidaTotal_Nacional(self):
        """TC_8 ESTE TEST CASE NECESITA FACTURAS CON STATUS  'ACOMODADA PENDIENTE DE ENTRADA' """
        #print("Test using: "+supplier)
        sge_funct = sge_functions2()
        print("------------------------------Test to Create PurchaseOrder_RecibidaTotal_Nacional")
        print("1	Ingresar a SGE con las credenciales <<User>> <Password>>")
        #sge_funct.login_adm_sge(login_data.adm_username, login_data.ip, login_data.adm_password)
        sge_funct.sge_connection(login_data.username, login_data.ip, login_data.password)
        conectado = sge_funct.validate_sge_connection()
        #conectado = sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial)
        if conectado:
            # print("1.1   cambiar usuario con permisos Teclando input  uu")
            # sge_funct.send_text("uu")
            # sge_funct.segundos_de_espera(1)
            # sge_funct.send_text("jmartin")
            print("2	Teclear input 	Enter")
            sge_funct.press_enter()
            print("3	Teclear input 	Enter")
            sge_funct.press_enter()
            print("4	Seleccionar <<Sucursal>>	12")
            sge_funct.send_text("12")
            print("5	Teclear input 	Enter")
            sge_funct.press_enter()
            print("6	Seleccionar <<OPCION MENU>>	2")
            sge_funct.send_text("2")
            print("7	Teclear input 	Enter")
            sge_funct.press_enter()
            print("8	Seleccionar <<OPCION MENU>>	4")
            sge_funct.send_text("4")
            print("9	Teclear input 	Enter")
            sge_funct.press_enter()
            print("10	Seleccionar <<OPCION MENU>>	2")
            sge_funct.send_text("2")
            print("11	Teclear input 	Enter")
            sge_funct.press_enter()
            print("12	Teclear input 	a")
            sge_funct.send_text("a")
            print("13	Presionar la combinacion de teclas: Ctrl + b ctrl+b")
            sge_funct.press_hotkeys("ctrl+b")
            sge_funct.segundos_de_espera(1)
            print("14 Ingresar <<proveedor>> configurado TENNECO")
            sge_funct.send_text("TENNECO")
            print("15	Teclear input 	Enter")
            sge_funct.press_enter()
            print("16  Buscar Factura configurada y pegarla")
            directorio_origen = files.inv_acomodado_pendiente_de_entrada_folder
            num_factura_acomodado_pendiente_de_entrada_folder, inv_factura_acomodado_pendiente_de_entrada_folder, nombre_archivo = sge_funct.obtener_factura_de_directorio(directorio_origen)
            # se envia el inv de po
            print(f"pegando {inv_factura_acomodado_pendiente_de_entrada_folder}")
            sge_funct.send_text(inv_factura_acomodado_pendiente_de_entrada_folder)
            sge_funct.segundos_de_espera(1)
            print("17	Teclear input 	Enter")
            sge_funct.press_enter()
            print("18 Presionar la combinacion de teclas: Ctrl + w ctrl+w")
            sge_funct.press_hotkeys("ctrl+w")
            sge_funct.segundos_de_espera(1)
            print("19 Presionar la combinacion de teclas: Ctrl + w ctrl+w")
            sge_funct.press_hotkeys("ctrl+w")
            sge_funct.segundos_de_espera(1)
            print("20	Teclear input 	Enter")
            sge_funct.press_enter()
            print("21 Presionar la combinacion de teclas: Ctrl + a ctrl+a")
            sge_funct.press_hotkeys("ctrl+a")
            sge_funct.segundos_de_espera(1)
            print("22 Teclear input  10")
            sge_funct.send_text("10")
            print("23 Teclear input  Enter")
            sge_funct.press_enter()
            print("24 Seleccionar <<OPCION MENU>> 2")
            sge_funct.send_text("2")
            print("25 Situarse en la orden de compra e ingresar el numero de PO. ")
            sge_funct.send_text(num_factura_acomodado_pendiente_de_entrada_folder)
            sge_funct.segundos_de_espera(1)
            print("26 Teclear input  Enter")
            sge_funct.press_enter()
            print("28 Teclear input  S")
            sge_funct.send_text("s")
            print("29 Teclear input  Enter")
            sge_funct.press_enter()
            print("Validating Purchase Order Status...")
            img_status = images.img_status_recibida_total
            nombre_status_esperado = "STATUS RECIBIDA TOTAL"
            if sge_funct.validar_po_status2(img_status, nombre_status_esperado):
                print(f"Status {nombre_status_esperado} validado correctamente")
                print("moviendo factura '/acomodado_pendiente_de_entrada' a '/recibido_total'")
                directorio_origen = files.inv_acomodado_pendiente_de_entrada_folder
                directorio_destino = files.inv_recibido_total_folder
                sge_funct.mover_facturas(num_factura_acomodado_pendiente_de_entrada_folder, directorio_origen, directorio_destino)
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
