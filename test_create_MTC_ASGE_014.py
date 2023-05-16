# FALTA FACTURA INVALIDA
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
    def test_MTC_ASGE_014(self):

        #print("Test using: "+supplier)
        sge_funct = sge_functions2()
        print("------------------------------Asignacion factura internacional valida")
        """TC14 ESTE TEST CASE NECESITA FACTURA VALIDA Y PO CON STATUS 'CONFIRMADA' CON DSO /SINDSO DE PREFERENCIA """

        print("iniciar sesion en servidor SFTP")
        print("Trying to establish SFTP Connection...")
        sge_funct.sftp_connection()
        print("Validating connection...")
        conectado = sge_funct.validate_sftp_connection()
        if conectado:
            # ____________________________________________BLOQUE SFTP
            print("1 Dentro del SFTP dirigirse a la <<RUTA>> cd /cacheJAVA/recibidos_uat/")
            sge_funct.send_text("cd /cacheJAVA/recibidos_uat/")
            print("2 Press Enter Enter")
            sge_funct.press_enter()
            print("3 Ingresar archivo de factura VALIDA en la carpeta de la ruta. subir_archivo")
            num_po_seleccionada, inv_factura_valida, archivo_seleccionado= sge_funct.subir_archivo_sftp2(files.internacionales_inv_valida_folder)
            print(num_po_seleccionada)
            print("4 Press Enter Enter")
            sge_funct.press_enter()
            print("5 salir de sftp exit")
            sge_funct.send_text("exit")
            print("6 Press Enter Enter")
            sge_funct.press_enter()
            # ____________________________________________BLOQUE SFTP
            # ____________________________________________BLOQUE SGE ADM EJECUTAR JOB
            print("7 iniciar sesion en SGE con usuario con permisos login_adm_sge")
            sge_funct.sge_connection(login_data.adm_username, login_data.ip, login_data.adm_password)
            print("8 Ejecutar JOB FACTURAS bash procesa_EDI.sh REC_INVOICE_TXT")
            sge_funct.send_text("bash procesa_EDI.sh REC_INVOICE_TXT")
            print("9 Press Enter Enter")
            sge_funct.press_enter()
            print("10 tiempo fuera 15 segundos")
            sge_funct.segundos_de_espera(15)
            job_status = images.img_status_job_psc_internacional_ok
            job_status_correcto = sge_funct.validar_job_status_x(job_status)
            if job_status_correcto:
                print("11 cerrar sesion de adm_sge exit")
                sge_funct.send_text("exit")
                print("12 Press Enter Enter")
                sge_funct.press_enter()
                print("13 tiempo fuera 2 segundos")
                sge_funct.segundos_de_espera(2)
                # ____________________________________________BLOQUE SGE ADM EJECUTAR JOB
                # ____________________________________________BLOQUE SGE PASOS USUARIO NORNAL
                print("14	Ingresar a SGE con las credenciales <<User>> <Password>>")
                # sge_funct.login_adm_sge(login_data.adm_username, login_data.ip, login_data.adm_password)
                sge_funct.sge_connection(login_data.username, login_data.ip, login_data.password)
                conectado = sge_funct.validate_sge_connection()
                if conectado:

                    print("6,Teclear input ,Enter")
                    sge_funct.press_enter()
                    print("7,Teclear input ,Enter")
                    sge_funct.press_enter()
                    print("8,Seleccionar <<Sucursal>>,12")
                    sge_funct.send_text("12")
                    print("9,Teclear input ,Enter")
                    sge_funct.press_enter()
                    print("10,Seleccionar <<OPCION MENU>>,2")
                    sge_funct.send_text("2")
                    print("11,Teclear input ,Enter")
                    sge_funct.press_enter()
                    print("12,Seleccionar <<OPCION MENU>>,4")
                    sge_funct.send_text("4")
                    print("13,Teclear input ,Enter")
                    sge_funct.press_enter()
                    print("14,Seleccionar <<OPCION MENU>>,10")
                    sge_funct.send_text("10")
                    print("15,Teclear input ,Enter")
                    sge_funct.press_enter()
                    print("16,Seleccionar <<OPCION MENU>>,2")
                    sge_funct.send_text("2")
                    print("17,Situarse en la orden de compra e ingresar el numero de PO.,")
                    sge_funct.send_text(num_po_seleccionada)
                    print("18,Teclear input ,Enter")
                    sge_funct.press_enter()
                    print("19,Teclear input ,S")
                    sge_funct.send_text("S")
                    print("20,Teclear input ,Enter")
                    sge_funct.press_enter()

                    print("Validating Purchase Order")
                    nombre_status_esperado = "EN TRANSITO"
                    img_status_transito = images.img_status_en_transito

                    if sge_funct.validar_po_status2(img_status_transito, nombre_status_esperado):
                        print(f"Status {nombre_status_esperado} validado correctamente")

                        print(
                            "MOVER po de 'facturas_internacionales/inv_valida a 'facturas_internacionales/en_transito'")
                        directorio_origen = files.internacionales_inv_valida_folder
                        directorio_destino = files.internacionales_en_transito_folder
                        sge_funct.mover_facturas(num_po_seleccionada, directorio_origen, directorio_destino)
                        # # GENERAR PO PSC RECIBIDA EN STATUS 10 REVISADA EN ORIGEN
                        # print(" Generando PO  PSC STATUS 10")
                        # num_status = "10"
                        # psc_path_destino = files.internacionales_revisada_en_origen_10_folder
                        # psc_number, psc_file_txt = sge_funct.crear_modificar_psc_status_xx(num_po_seleccionada, psc_path_destino, num_status)
                        #
                        # # quitar psc de carpeta
                        # psc_path_origen = files.internacionales_confirmada_03_SINDSO_folder
                        # sge_funct.remove_file(psc_path_origen, psc_file_txt)
                        # crear num_po.txt
                        sge_funct.crear_nombre_po_txt_tmp(num_po_seleccionada)
                    else:
                        print("Fallo validacion, estatus Incorrecto")
                        assert False, "Fallo validacion, estatus Incorrecto"
                    # ____________________________________________BLOQUE SGE VALIDAR STATUS
        else:
            print(conectado)
            assert conectado, "error de conexion"

    def tearDown(self):
        sge_funct = sge_functions2()
        #sge_funct.terminate_sge_session()

if __name__ == '__main__':
    unittest.main()

