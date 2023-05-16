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
    def test_PurchaseOrder_ProcesodeAcomodo_Internacional(self):


        sge_funct = sge_functions2()
        print("1,Ingresar a SGE con el usuario de perfil almacen con las credenciales <<User>> <Password>>,")
        sge_funct.sge_connection(login_data.username, login_data.ip, login_data.password)
        conectado = sge_funct.validate_sge_connection()
        if conectado:
       
            print("2,Teclear input ,Enter")
            sge_funct.press_enter()
            print("3,Teclear input ,Enter")
            sge_funct.press_enter()
            print("4,Seleccionar <<Sucursal>>,12")
            sge_funct.send_text("12")
            print("5,Teclear input ,Enter")
            sge_funct.press_enter()
            print("6,Seleccionar <<OPCION MENU>>,2")
            sge_funct.send_text("2")
            print("7,Teclear input ,Enter")
            sge_funct.press_enter()
            print("8,Seleccionar <<OPCION MENU>>,4")
            sge_funct.send_text("4")
            print("9,Teclear input ,Enter")
            sge_funct.press_enter()
            print("10,Seleccionar <<OPCION MENU>>,10")
            sge_funct.send_text("10")
            print("11,Teclear input ,Enter")
            sge_funct.press_enter()
            print("12,Seleccionar <<OPCION MENU>>,2")
            sge_funct.send_text("2")
            print("14,Situarse en la orden de compra e ingresar el numero de PO.,rclick")
            sge_funct.send_text()
            print("15,Teclear input ,Enter")
            sge_funct.press_enter()
            print("16,Teclear input ,S")
            sge_funct.send_text("s")
            print("17,Teclear input ,Enter")
            sge_funct.press_enter()
            print("18,Dirigirse a la secuencia 001,flechaabajo")
            sge_funct.press_hotkeys("ctrl+down")
            print("19,Presionar la combinacion de teclas: Ctrl + k,ctrl+k")
            sge_funct.press_hotkeys("ctrl+k")
            print("20,Ingresar el usuario almacen,<<USUARIOALMACEN>>")
            sge_funct.send_text("jmartin")
            print("21,Teclear input ,Enter")
            sge_funct.press_enter()

            print("Validating Purchase Order creation")
            #CAMBIAR IMAGEN EN PROCESO DE ACOMOD
            img_status = images.img_status_en_transito
            nombre_status_esperado = "EN PROCESO DE ACOMOD"
            if sge_funct.validar_po_status2(img_status, nombre_status_esperado):
                print(f"Status {nombre_status_esperado} validado correctamente")
                # revisar nombre de archivo
                print(" MODIFICANDO PO PSC STATUS En transito nacional (16)")
                nuevo_status = "16"
                psc_path_origen = f"{files.internacionales_revisada_12_folder}{psc_select_txt}"
                psc_path_destino = files.internacionales_revisada_12_folder
                psc_number, psc_file_txt = sge_funct.crear_modificar_psc_status_xx(po_seleccionada,
                                                                                   psc_path_origen,
                                                                                   psc_path_destino,
                                                                                   nuevo_status, psc_select_txt)
                print("MOVER el archivo PSC generado a carpeta de estatus correspondiente")

                print(
                    "REMOVE po PSC con status 10 de 'facturas_internacionales/revisada_en_origen_10'")
                sge_funct.remove_file(files.internacionales_revisada_en_origen_10_folder, psc_select_txt)
                # eliminar factura en trasito utilizada en job?
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
