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
    def test_MTC_ASGE_015(self):

        #print("Test using: "+supplier)
        sge_funct = sge_functions2()
        print("------------------------------Asignacion factura internacional revision")

        """TC15 ESTE TEST CASE NECESITA FACTURA INVALIDA Y PO CON STATUS 'CONFIRMADA' """
        # print("Test using: "+supplier)
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
            print("3 Ingresar archivo de factura INVALIDA en la carpeta de la ruta. subir_archivo")
            num_po_seleccionada, inv_factura_invalida, archivo_seleccionado= sge_funct.subir_archivo_sftp2(files.internacionales_inv_invalida_folder)
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
            # deberia ser pend. ejercutar hasta aqui la primera vez
            job_status = images.img_status_job_pend
            job_status_correcto = sge_funct.validar_job_status_x(job_status)
            if job_status_correcto:
                #num_po_seleccionada= "012A0021200347RD"
                print("11 cerrar sesion de adm_sge exit")
                sge_funct.send_text("exit")
                print("12 Press Enter Enter")
                sge_funct.press_enter()
                print("13 tiempo fuera 2 segundos")
                sge_funct.segundos_de_espera(2)
                # # ____________________________________________BLOQUE SGE ADM EJECUTAR JOB
                # ____________________________________________BLOQUE SGE PASOS USUARIO NORNAL
                print("14	Ingresar a SGE con las credenciales <<User>> <Password>>")
                # sge_funct.login_adm_sge(login_data.adm_username, login_data.ip, login_data.adm_password)
                sge_funct.sge_connection(login_data.username, login_data.ip, login_data.password)
                conectado = sge_funct.validate_sge_connection()
                #conectado = sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial)
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
                    print("16,Seleccionar <<OPCION MENU>>,6")
                    sge_funct.send_text("6")
                    print("17,Hacer la busqueda de la factura en la pantalla pegando el numero de factura en el campo factura,clic derecho")
                    # usar inv
                    #inv_factura_invalida = "INV012A0021200347RD"
                    sge_funct.send_text(inv_factura_invalida)
                    print("18,Presionar la combinacion de teclas: Ctrl + R,ctrl+r")
                    sge_funct.press_hotkeys("ctrl+r")
                    print("19,Presionar la combinacion de teclas: Ctrl + K,ctrl+k")
                    sge_funct.press_hotkeys("ctrl+k")
                    print("20,Ingresar en Login <<UsuarioAdmin>> y la contraseña  <<PassAdmin>> del usuario con permiso de autorizar, <<UsuarioAdmin>>,<< PassAdmin >> ")
                    sge_funct.send_text("grejudl")
                    print("21,Teclear input ,Enter")
                    sge_funct.press_enter()
                    sge_funct.send_text("123")
                    print("22,Teclear input ,Enter")
                    sge_funct.press_enter()
                    sge_funct.segundos_de_espera(2)
                    sge_funct.press_enter()
                    #******************************
                    print("23,Presionar la combinacion de teclas: Ctrl + a,ctrl+a")
                    sge_funct.press_hotkeys("ctrl+a")
                    print("24,Seleccionar <<OPCION MENU>>,2")
                    sge_funct.send_text("2")
                    print("25,Abrir y copiar contenido de archivo <<Archivo INV-ordenCompra.txt>>,numero de PO.")
                    # num_po_seleccionada?
                    sge_funct.send_text(num_po_seleccionada)
                    print("26,Teclear input ,Enter")
                    sge_funct.press_enter()
                    print("27,Teclear input ,S")
                    sge_funct.send_text("S")
                    print("28,Teclear input ,Enter")
                    sge_funct.press_enter()
                    print("Validating Purchase Order")
                    nombre_status = "EN TRANSITO DESDE PROVEEDOR" #estatus final del TC15
                    img_status = images.img_status_en_transito
                    nombre_status_esperado = "EN TRANSITO DESDE PROVEEDOR"
                    if sge_funct.validar_po_status2(img_status, nombre_status):
                        print(f"Status {nombre_status_esperado} validado correctamente")

                        print(
                            "MOVER po de 'facturas_internacionales/inv_invalida' a 'facturas_internacionales/en_transito'")
                        directorio_origen = files.internacionales_inv_invalida_folder
                        directorio_destino = files.internacionales_en_transito_folder
                        sge_funct.mover_facturas(num_po_seleccionada, directorio_origen, directorio_destino)
                    else:
                        print("Fallo validacion, estatus Incorrecto")
                        assert False, "Fallo validacion, estatus Incorrecto"
                    #____________________________________________BLOQUE SGE VALIDAR STATUS
            else:
                print(conectado)
                assert conectado, "error de conexion"

    def tearDown(self):
        sge_funct = sge_functions2()
        sge_funct.terminate_sge_session()

if __name__ == '__main__':
    unittest.main()

