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


        sge_funct = sge_functions2()
        print("1 Ingresar a SGE con las credenciales <<User>> <Password>> ")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        conectado = sge_funct.validate_sge_connection()
        if conectado:
       
            print("2 Teclear input  Enter")
            sge_funct.press_enter()
            print("3 Teclear input  Enter")
            sge_funct.press_enter()
            print("4 Seleccionar <<Sucursal>> 12")
            print("5 Teclear input  Enter")
            sge_funct.press_enter()
            print("6 Seleccionar <<OPCION MENU>> 2")
            print("7 Teclear input  Enter")
            sge_funct.press_enter()
            print("8 Seleccionar <<OPCION MENU>> 4")
            print("9 Teclear input  Enter")
            sge_funct.press_enter()
            print("10 Seleccionar <<OPCION MENU>> 2")
            print("11 Teclear input  Enter")
            sge_funct.press_enter()
            print("12 Ingresar input a")
            print("13 Presionar la combinacion de teclas: Ctrl + b ctrl+b")
            sge_funct.press_hotkeys("ctrl+b")
            print("14 Ingresar <<proveedor>> configurado ")
            print("15 Teclear input  Enter")
            sge_funct.press_enter()
            print("16 Buscar la factura configurada ")
            print("17 Teclear input  Enter")
            sge_funct.press_enter()
            print("18 Presionar la combinacion de teclas: Ctrl + w ctrl+w")
            sge_funct.press_hotkeys("ctrl+w")
            print("19 Presionar la combinacion de teclas: Ctrl + w ctrl+w")
            sge_funct.press_hotkeys("ctrl+w")
            print("20 Teclear input  Enter")
            sge_funct.press_enter()
            print("21 Presionar la combinacion de teclas: Ctrl + a ctrl+a")
            sge_funct.press_hotkeys("ctrl+a")
            print("22 Teclear input  10")
            print("23 Teclear input  Enter")
            sge_funct.press_enter()
            print("24 Seleccionar <<OPCION MENU>> 2")
            print("25 Situarse en la orden de compra e ingresar el numero de PO. rclick")
            print("26 Teclear input  Enter")
            sge_funct.press_enter()
            print("27 Teclear input  S")
            print("28 Teclear input  Enter")
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
