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
    def test_PurchaseOrder_Confirmacion_Internacional_DSO(self):
        """TC_13  """
        print("------------------------------Test to Create PurchaseOrder_Confirmacion_Internacional_DSO")
        #print("Test using: "+supplier)
        sge_funct = sge_functions2()
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
            print("3 Ingresar archivo de cambios de estatus PSC. subirpsc status 03")
            num_po_seleccionada, inv_po_seleccionada, random_po_txt = sge_funct.subir_po_sftp_internacional(files.internacionales_por_confirmar_03_DSO_folder)
            print(f"psc status 03 seleccionado: {random_po_txt}")
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
            print("8 Ejecutar JOB FACTURAS bash procesa_EDI.sh REC_ESTATUS_TXT")
            sge_funct.send_text("bash procesa_EDI.sh REC_ESTATUS_TXT")
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
                # conectado = sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial)
                if conectado:

                    print("15	Teclear input 	Enter")
                    sge_funct.press_enter()
                    print("16	Teclear input 	Enter")
                    sge_funct.press_enter()
                    print("17	Seleccionar <<Sucursal>>	12")
                    sge_funct.send_text("12")
                    print("18	Teclear input 	Enter")
                    sge_funct.press_enter()
                    print("19	Seleccionar <<OPCION MENU>>	2")
                    sge_funct.send_text("2")
                    print("20	Teclear input 	Enter")
                    sge_funct.press_enter()
                    print("21	Seleccionar <<OPCION MENU>>	4")
                    sge_funct.send_text("4")
                    print("22	Teclear input 	Enter")
                    sge_funct.press_enter()
                    print("23	Seleccionar <<OPCION MENU>>	10")
                    sge_funct.send_text("10")
                    print("24	Teclear input 	Enter")
                    sge_funct.press_enter()
                    print("25	Seleccionar <<OPCION MENU>>	2")
                    sge_funct.send_text("2")
                    print("26   Situarse en la orden de compra e ingresar el numero de PO.")
                   # num_po_por_confirmar = "012A00212003410A"
                    sge_funct.send_text(num_po_seleccionada)
                    print("27	Teclear input 	Enter")
                    sge_funct.press_enter()
                    print("28	Teclear input 	s")
                    sge_funct.send_text("s")
                    print("29	Teclear input 	Enter")
                    sge_funct.press_enter()
                    sge_funct.segundos_de_espera(3)
                    # ____________________________________________BLOQUE SGE PASOS USUARIO NORNAL
                    # ____________________________________________BLOQUE SGE VALIDAR STATUS
                    print("Validating Purchase Order Status...")
                    img_status = images.img_status_confirmada_por_proveedor
                    nombre_status_esperado = "CONFIRMADO POR PROVEEDOR"
                    if sge_funct.validar_po_status2(img_status, nombre_status_esperado):
                        print(f"Status {nombre_status_esperado} validado correctamente")
                        print("MOVER po de 'facturas_internacionales/por_confirmar_03_DSO' a 'facturas_internacionales/confirmada_03_DSO'")
                        directorio_origen = files.internacionales_por_confirmar_03_DSO_folder
                        directorio_destino = files.internacionales_confirmada_03_DSO_folder
                        sge_funct.mover_po_internacionales(num_po_seleccionada, directorio_origen, directorio_destino)
                        # print(f"CREAR INV validas e Invalidas para la PO: {num_po_seleccionada}")
                        # sge_funct.crear_factura_valida_e_invalida_txt()

                    else:
                        print("Fallo validacion, estatus Incorrecto")
                        assert False, "Fallo validacion, estatus Incorrecto"
                    # ____________________________________________BLOQUE SGE VALIDAR STATUS
        else:
            print(conectado)
            assert conectado, "error de conexion"

    def tearDown(self):
        sge_funct = sge_functions2()
        sge_funct.terminate_sge_session()


if __name__ == '__main__':
    unittest.main()
