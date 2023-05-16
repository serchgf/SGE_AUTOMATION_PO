import unittest
from Config.config import login_data, images, csv_files_path, files
from sge_functions.sge_functions import sge_functions
from Config.config import csv_files_path
from Config.config import txt_files_path
from ddt import ddt, file_data
from sge_functions.sge_functions2 import sge_functions2

#@ddt
class SgePoUnittest(unittest.TestCase):

    #@file_data("./Config/TestDataset/dataSet_ddt_po.json")
    def test_MTC_ASGE_024(self):

        #print("Test using: "+supplier)
        sge_funct = sge_functions2()
        print("------------------------------Recibida Revision Internacional")

        """TC24 ESTE TEST CASE NECESITA PO CON STATUS 'TRANSITO NACIONAL (16)' """
        print("1 Ingresar a SGE con las credenciales <<User>> <Password>>")
        #conectado = sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial)
        sge_funct.sge_connection(login_data.username, login_data.ip, login_data.password)
        conectado = sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial)
        if conectado:

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
            print("13,Situarse en la orden de compra e ingresar el numero de PO.")
            num_po_seleccionada, inv_po_seleccionada, psc_select_txt = sge_funct.obtener_datos_psc_file(
                files.internacionales_en_transito_nacional_16)
            # num_po
            sge_funct.send_text(num_po_seleccionada)
            print("14,Teclear input ,Enter")
            sge_funct.press_enter()
            print("15,Teclear input ,S")
            sge_funct.send_text("S")
            print("16,Teclear input ,Enter")
            sge_funct.press_enter()
            print("17,Dirigirse a la secuencia 001 ,flechaabajo")
            sge_funct.press_hotkeys("ctrl+down")
            print("18,Presionar la combinacion de teclas: Ctrl + c")
            sge_funct.press_hotkeys("ctrl+c")
            print("19,Presionar la combinacion de teclas: Ctrl + o")
            sge_funct.press_hotkeys("ctrl+o")
            print("Seleccionar el numero de pedimento copiandolo en el portapapeles")
            #double click obtener coordenadas de num_pedimento

            print("20 Presionar la combinacion de teclas: 'Ctrl + a'  ctrl+a")
            sge_funct.press_hotkeys("ctrl+a")
            print("21 Presionar la combinacion de teclas: 'Ctrl + a'  ctrl+a")
            sge_funct.press_hotkeys("ctrl+a")
            print("22 Presionar la combinacion de teclas: 'Ctrl + a'  ctrl+a")
            sge_funct.press_hotkeys("ctrl+a")
            print("21,Teclear input ,Enter")
            sge_funct.press_enter()
            print("22,Teclear input ,8")
            sge_funct.send_text("8")
            print("Ingresar nombre proveedor Internacional <<OREILLY>>")
            sge_funct.send_text("USMEXICO")#???
            print("21,Teclear input ,Enter")
            sge_funct.press_enter()
            print("Pegar numero de pedimento del portapapeles rclick")
            # num_pedimento usar send_text? o obtener imagen rclick
            sge_funct.send_text(num_po_seleccionada)
            print("22 Presionar la combinacion de teclas: 'Ctrl + w'  ctrl+w")
            sge_funct.press_hotkeys("ctrl+w")
            print("Pegar numero de papeleta rclick")
            # generar archivo o numero aleatorio y validar imagen de aceptacion, crear funcion con ciclo while
            sge_funct.send_text("numero de papeleta")
            print("21,Teclear input ,Enter")
            sge_funct.press_enter()

            print("Validating Purchase Order")
            # nombre_status_esperado = "NUMERO PAPELETA RECIBIDA EN P" # es el mismo status que el anterior?
            # # OBTENER IMAGEN NUMERO PAPELETA RECIBIDA EN P
            # img_status = images.img_status_pedimento_pagado
            # if sge_funct.validar_po_status2(img_status, nombre_status_esperado):
            #     print(f"Status {nombre_status_esperado} validado correctamente")
            #     # eliminar PSC status 14
            #     print("eliminando psc procesada status 14...")
            #     path_archivo_origen = files.internacionales_pedimento_pagado_13_folder #MOD
            #     sge_funct.remove_file(path_archivo_origen, psc_select_txt)
            #
            # else:
            #     print("Fallo validacion, estatus Incorrecto")
            #     assert False, "Fallo validacion, estatus Incorrecto"
            #     # ____________________________________________BLOQUE SGE VALIDAR STATUS
        else:
            print(conectado)
            assert conectado, "error de conexion"

    def tearDown(self):
        sge_funct = sge_functions2()
        # sge_funct.terminate_sge_session()

if __name__ == '__main__':
    unittest.main()

