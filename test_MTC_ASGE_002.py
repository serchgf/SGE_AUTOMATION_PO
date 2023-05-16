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
    def test_PurchaseOrder_Creacion_Nacional_DSO(self):

        print("Test Case 01 PurchaseOrder_Creacion_Nacional_DSO")
        sge_funct = sge_functions2()
        print("1,Ingresar a SGE con el usuario de perfil itmx12 con las credenciales <<User>> <Password>>,")
        sge_funct.sge_connection(login_data.username, login_data.ip, login_data.password)
        conectado = sge_funct.validate_sge_connection()
        if conectado:
            # ### """"""""""""""""""""""""""""""""""""""""""""
            print("1 Teclear input  Enter")
            sge_funct.press_enter()
            print("2 Teclear input  Enter")
            sge_funct.press_enter()
            print("3 Seleccionar <<Sucursal>> 12")
            sge_funct.send_text("12")
            print("4 Teclear input  Enter")
            sge_funct.press_enter()
            print("5 Seleccionar <<OPCION MENU>> 2")
            sge_funct.send_text("2")
            print("6 Teclear input  Enter")
            sge_funct.press_enter()
            print("7 Seleccionar <<OPCION MENU>> 4")
            sge_funct.send_text("4")
            print("8 Teclear input  Enter")
            sge_funct.press_enter()
            print("9 Seleccionar <<OPCION MENU>> 10")
            sge_funct.send_text("10")
            print("10 Teclear input  Enter")
            sge_funct.press_enter()
            # ###""""""""""""""""""""""""""""""""""""""""""""
            print("11 Seleccionar <<OPCION MENU>> 1")
            sge_funct.send_text("1")
            print("12 Situarse en Proveedor y dar click en la combinacion Ctrl + E ctrl+e")
            sge_funct.press_hotkeys("ctrl+e")
            print("13 Teclear primeras letras del proveedor configurado <<Proveedor>> TENNECO")
            sge_funct.send_text("TENNECO")
            print("14 Teclear input  Enter")
            sge_funct.press_enter()
            print("15 Situarse en Desglosar DSO presionando la tecla tab 4 veces tab")
            sge_funct.press_tab()
            sge_funct.press_tab()
            sge_funct.press_tab()
            sge_funct.press_tab()
            print("15 Teclear input  s")
            sge_funct.send_text("s")
            print("16 Presionar la combinacion de teclas: Ctrl + W ctrl+w")
            sge_funct.press_hotkeys("ctrl+w")
            print("17 Abrir y copiar contenido de archivo <<Datos_productos_po.txt>> read_file")
            datos_productos_po_txt = txt_files_path.txt_datos_productos_po
            sge_funct.leer_archivo_productos(datos_productos_po_txt)
            print("18 Presionar la combinacion de teclas: Ctrl + W ctrl+w")
            sge_funct.press_hotkeys("ctrl+w")
            print("19 Presionar la combinacion de teclas: Ctrl + W ctrl+w")
            sge_funct.press_hotkeys("ctrl+w")
            print("20 Ingresar en Login de el <<Usuario>> sfabian")
            sge_funct.send_text("sfabian")
            print("21 Teclear input  Enter")
            sge_funct.press_enter()
            print("26 Presionar la combinacion de teclas: Ctrl + W ctrl+w")
            sge_funct.press_hotkeys("ctrl+w")
            print("27 Presionar la combinacion de teclas: Ctrl + W ctrl+w")
            sge_funct.press_hotkeys("ctrl+w")
            print("28 Seleccionar la Orden de compra dando input doubleclick")
            img_doubleclick = images.img_inicio_orden_de_compra
            sge_funct.doubleClick(img_doubleclick)
            print("29 Teclear input  Enter")
            sge_funct.press_enter()
            print("30 Teclear input  2")
            sge_funct.send_text("2")
            print("31 Situarse en la orden de compra e ingresar el numero de PO. rclick")
            img_rclick = images.img_consulta_orden_de_compra
            sge_funct.rightClick(img_rclick)
            print("32 Teclear input  Enter")
            sge_funct.press_enter()
            print("33 Teclear input  s")
            sge_funct.send_text("s")
            print("34 Teclear input  Enter")
            sge_funct.press_enter()
            print("35 Presionar la combinacion de teclas: Ctrl + K ctrl+k")
            sge_funct.press_hotkeys("ctrl+k")
            print("36 Ingresar en Login el <<UsarioCompras>> sfabian")
            sge_funct.send_text("sfabian")
            print("37 Teclear input  Enter")
            sge_funct.press_enter()
            print("38 tiempo_fuera 20 segundos")
            sge_funct.segundos_de_espera(20)
            print("39 Presionar la combinacion de teclas: Ctrl + K ctrl+k")
            sge_funct.press_hotkeys("ctrl+k")
            print("40 Ingresar en Login el <<UsarioCompras>> sfabian")
            sge_funct.send_text("sfabian")
            print("41 Teclear input  Enter")
            sge_funct.press_enter()


            print("Validating Purchase Order creation")
            nombre_status = "confirmada por proveedor"
            img_status_confirmada = images.img_status_confirmada_por_proveedor

            if sge_funct.validar_po_status2(img_status_confirmada, nombre_status):
                print(f"Status {nombre_status} validado correctamente")
                print("Creando archivos: factura valida y factura invalida")
                #en carpetas de tmp
                sge_funct.crear_factura_valida_e_invalida_txt()
            else:
                print("Fallo validacion, estatus Incorrecto")
                assert False, "Fallo validacion, estatus Incorrecto"

        else:
            print(conectado)
            assert False, "Connection Failed!"



    def tearDown(self):
        sge_funct = sge_functions()
        sge_funct.terminate_sge_session()


if __name__ == '__main__':
    unittest.main()
