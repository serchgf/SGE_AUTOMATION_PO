import unittest
from Config.config import login_data, images, csv_files_path
from sge_functions.sge_functions import sge_functions
from Config.config import csv_files_path
from Config.config import txt_files_path
from ddt import ddt, file_data
from sge_functions.sge_functions2 import sge_functions2

#@ddt
class SgePoUnittest(unittest.TestCase):

    #@file_data("./Config/TestDataset/dataSet_ddt_po.json")
    def test_PurchaseOrder_Creacion_Nacional_SINDSO(self):

        #print("Test using: "+supplier)

        print("------------------------------Test to Create Purchase Order Nacional_SINDSO")

        """TC6 ESTE TEST CASE NECESITA FACTURAS CON STATUS  'EN TRANSITO' """
        # print("Test using: "+supplier)
        sge_funct = sge_functions2()
        print("1	Teclear input 	Enter")
        sge_funct.sge_connection(login_data.username, login_data.ip, login_data.password)
        conectado = sge_funct.validate_sge_connection()
        if conectado:
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
            print("10	Seleccionar <<OPCION MENU>>	10")
            sge_funct.send_text("10")
            print("11	Teclear input 	Enter")
            sge_funct.press_enter()
            print("12	Seleccionar <<OPCION MENU>>	1")
            sge_funct.send_text("1")
            print("13   Presionar la combinacion de teclas: Ctrl + e")
            sge_funct.press_hotkeys("ctrl+e")
            print("14	Teclear primeras letras del proveedor configurado <<Proveedor>>")
            sge_funct.send_text("TENNECO")
            print("15	Teclear input 	Enter")
            sge_funct.press_enter()
            print("19   Situarse en 'Desglosar DSO' presionando la tecla 'tab' 4 veces")
            sge_funct.press_tab()
            sge_funct.press_tab()
            sge_funct.press_tab()
            sge_funct.press_tab()
            print("16	Teclear input 	n")
            sge_funct.send_text("n")
            print("17   Presionar la combinacion de teclas: Ctrl + w")
            sge_funct.press_hotkeys("ctrl+w")
            print("Ingresar en Login el <<UsarioCompras>>  sfabian")
            sge_funct.send_text("sfabian")
            print("18	Teclear input 	Enter")
            sge_funct.press_enter()
            print("Abrir y copiar contenido de archivo <<Datos_productos_po.txt>>")
            datos_productos_po_txt = txt_files_path.txt_datos_productos_po
            sge_funct.leer_archivo_productos(datos_productos_po_txt)
            print("19   Presionar la combinacion de teclas: Ctrl + w")
            sge_funct.press_hotkeys("ctrl+w")
            print("20   Presionar la combinacion de teclas: Ctrl + w")
            sge_funct.press_hotkeys("ctrl+w")
            print("Ingresar en Login el <<UsarioCompras>>  sfabian")
            sge_funct.send_text("sfabian")
            print("21	Teclear input 	Enter")
            sge_funct.press_enter()
            print("22   Presionar la combinacion de teclas: Ctrl + w")
            sge_funct.press_hotkeys("ctrl+w")
            print("23   Presionar la combinacion de teclas: Ctrl + w")
            sge_funct.press_hotkeys("ctrl+w")
            print("24  Seleccionar la Orden de compra dando input  doubleclick")
            img_doubleclick = images.img_inicio_orden_de_compra
            sge_funct.doubleClick(img_doubleclick)
            print("25	Teclear input 	Enter")
            sge_funct.press_enter()
            print("26	Teclear input 	2")
            sge_funct.send_text("2")
            print("Situarse en la orden de compra e ingresar el numero de PO.")
            img_rclick = images.img_consulta_orden_de_compra
            sge_funct.rightClick(img_rclick)
            print("27	Teclear input 	Enter")
            sge_funct.press_enter()
            print("28	Teclear input 	s")
            sge_funct.send_text("s")
            print("29	Teclear input 	Enter")
            sge_funct.press_enter()
            print("30   Presionar la combinacion de teclas: Ctrl + k")
            sge_funct.press_hotkeys("ctrl+k")
            print("31   Ingresar en Login el <<UsarioCompras>>  sfabian")
            sge_funct.send_text("sfabian")
            print("32	Teclear input 	Enter")
            sge_funct.press_enter()
            sge_funct.segundos_de_espera(3)
            print("33  Presionar la combinacion de teclas: Ctrl + k")
            sge_funct.press_hotkeys("ctrl+k")
            print("34 Ingresar usuario sfabian")
            sge_funct.send_text("sfabian")
            print("35	Teclear input 	Enter")
            sge_funct.press_enter()

            print("Validating Purchase Order creation")
            nombre_status = "confirmada por proveedor"
            img_status_confirmada = images.img_status_confirmada_por_proveedor

            if sge_funct.validar_po_status2(img_status_confirmada, nombre_status):
                print(f"Status {nombre_status} validado correctamente")
                print("Creando archivos: factura valida y factura invalida")
                sge_funct.crear_factura_valida_e_invalida_txt()
            else:
                print("Fallo validacion, estatus Incorrecto")
                assert False, "Fallo validacion, estatus Incorrecto"

        else:
            print(conectado)
            assert False, "Connection Failed!"

    def tearDown(self):
        sge_funct = sge_functions()
        #sge_funct.terminate_sge_session()


if __name__ == '__main__':
    unittest.main()
