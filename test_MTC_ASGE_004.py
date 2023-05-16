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
    def test_PurchaseOrder_AsignacionFactura_Nacional_Revision(self):

        print("Test Case 04 PPurchaseOrder_AsignacionFactura_Nacional_Revision")
        sge_funct = sge_functions2()
        print("iniciar sesion en servidor SFTP")
        print("Trying to establish SFTP Connection...")
        sge_funct.sftp_connection()
        print("Validating connection...")
        conectado = sge_funct.validate_sftp_connection()

        if conectado:
            print("1 Dentro del SFTP dirigirse a la <<RUTA>> cd /cacheJAVA/recibidos_uat/")
            sge_funct.send_text("cd /cacheJAVA/recibidos_uat/")
            print("2 Press Enter Enter")
            sge_funct.press_enter()
            print("3 Ingresar archivo de factura INVALIDA en la carpeta de la ruta. subir_archivo")
            num_factura_invalida, inv_factura_invalida, archivo_seleccionado = sge_funct.subir_archivo_sftp2(files.inv_invalidas_folder)
            print("4 Press Enter Enter")
            sge_funct.press_enter()
            print("5 salir de sftp exit")
            sge_funct.send_text("exit")
            print("6 Press Enter Enter")
            sge_funct.press_enter()
            ### bloque 2
            print("7 iniciar sesion en SGE con usuario con permisos login_adm_sge")
            sge_funct.sge_connection(login_data.adm_username, login_data.ip, login_data.adm_password)
            print("8 Ejecutar JOB FACTURAS bash procesa_EDI.sh REC_INVOICE_TXT")
            sge_funct.send_text("bash procesa_EDI.sh REC_INVOICE_TXT")
            print("9 Press Enter Enter")
            sge_funct.press_enter()
            print("10 tiempo fuera 15 segundos")
            sge_funct.segundos_de_espera(15)
            print("11 cerrar sesion de adm_sge exit")
            sge_funct.send_text("exit")
            print("12 Press Enter Enter")
            sge_funct.press_enter()
            print("13 tiempo fuera 2 segundos")
            sge_funct.segundos_de_espera(2)
            ### bloque 2
            ### bloque 3
            print("14 Ingresar a SGE con las credenciales <<User>> <Password>> login_sge")
            sge_funct.sge_connection(login_data.username, login_data.ip, login_data.password)
            print("15 Teclear input  Enter")
            sge_funct.press_enter()
            print("16 Teclear input  Enter")
            sge_funct.press_enter()
            print("17 Seleccionar <<Sucursal>> 12")
            sge_funct.send_text("12")
            print("18 Teclear input  Enter")
            sge_funct.press_enter()
            print("19 Seleccionar <<OPCION MENU>> 2")
            sge_funct.send_text("2")
            print("20 Teclear input  Enter")
            sge_funct.press_enter()
            print("21 Seleccionar <<OPCION MENU>> 4")
            sge_funct.send_text("4")
            print("22 Teclear input  Enter")
            sge_funct.press_enter()
            print("23 Seleccionar <<OPCION MENU>> 10")
            sge_funct.send_text("10")
            print("24 Teclear input  Enter")
            sge_funct.press_enter()
            print("25 Seleccionar <<OPCION MENU>> 6")
            sge_funct.send_text("6")
            print("26 Situarse en la orden de compra e ingresar el numero de PO. pegar_num_po")
            sge_funct.send_text(inv_factura_invalida)
            print("27  ctrl+r")
            sge_funct.press_hotkeys("ctrl+r")
            print("28  ctrl+k")
            sge_funct.press_hotkeys("ctrl+k")
            print("29 escribir usuario adm grejudl")
            sge_funct.send_text("grejudl")
            print("30 Teclear input  Enter")
            sge_funct.press_enter()
            print("31 escribir autorizacion adm 123")
            sge_funct.send_text("123")
            print("32 Teclear input  Enter")
            sge_funct.press_enter()
            print("33 Teclear input  Enter")
            sge_funct.press_enter()
            print("34 tiempo fuera 2 segundos")
            sge_funct.segundos_de_espera(2)
            print("35 Presionar la combinacion de teclas: Ctrl + a ctrl+a")
            sge_funct.press_hotkeys("ctrl+a")
            print("36 tiempo fuera 2 segundos")
            sge_funct.segundos_de_espera(2)
            print("37 Seleccionar <<OPCION MENU>> 2")
            sge_funct.send_text("2")
            print("38 Abrir y copiar contenido de archivo <<Archivo INV-ordenCompra.txt>> pegar_num_po")
            sge_funct.send_text(num_factura_invalida)
            print("39 Teclear input  Enter")
            sge_funct.press_enter()
            print("40 Teclear input  s")
            sge_funct.send_text("s")
            print("41 Teclear input  Enter")
            sge_funct.press_enter()
            print("Validating Purchase Order creation")
            img_status = images.img_status_en_transito
            nombre_status = "EN TRANSITO"

            if sge_funct.validar_po_status2(img_status, nombre_status):
                print("Validating Status 'En transito'")
                if sge_funct.re_validate_status(img_status):
                    print("validado correctamente")
                    directorio_origen = files.inv_invalidas_folder
                    directorio_destino = files.inv_en_transito_folder
                    sge_funct.mover_facturas(num_factura_invalida, directorio_origen, directorio_destino)
                else:
                    print("Fallo validacion, estatus Incorrecto")

        else:
            print(conectado)
            assert False, "Connection Failed!"

    def tearDown(self):
        sge_funct = sge_functions()
        sge_funct.terminate_sge_session()

    if __name__ == '__main__':
        unittest.main()
