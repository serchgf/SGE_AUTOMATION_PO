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
        print("1,Ingresar a SGE con el usuario de perfil almacen con las credenciales <<User>> <Password>>,")
        sge_funct.sge_connection(login_data.username, login_data.ip, login_data.password)
        conectado = sge_funct.validate_sge_connection()
        if conectado:

            print("2 Teclear input  Enter")
            sge_funct.press_enter()
            print("3 Teclear input  Enter")
            sge_funct.press_enter()
            print("4 Seleccionar <<Sucursal>> 12")
            sge_funct.send_text("12")
            print("5 Teclear input  Enter")
            sge_funct.press_enter()
            print("6 Seleccionar <<OPCION MENU>> 2")
            sge_funct.send_text("2")
            print("7 Teclear input  Enter")
            sge_funct.press_enter()
            print("8 Seleccionar <<OPCION MENU>> 4")
            sge_funct.send_text("4")
            print("9 Teclear input  Enter")
            sge_funct.press_enter()
            print("10 Seleccionar <<OPCION MENU>> 10")
            sge_funct.send_text("10")
            print("11 Teclear input  Enter")
            sge_funct.press_enter()
            print("12 Seleccionar <<OPCION MENU>> 2")
            sge_funct.send_text("2")
            print("14 Situarse en la orden de compra e ingresar el numero de PO. rclick")
            sge_funct.send_text()
            print("15 Teclear input  Enter")
            sge_funct.press_enter()
            print("16 Teclear input  S")
            sge_funct.send_text("s")
            print("17 Teclear input  Enter")
            sge_funct.press_enter()

            print("Validating Purchase Order")
            # CAMBIAR IMAGEN Acomodado Pendiente de Paridad
            img_status = images.img_status_en_transito
            nombre_status_esperado = "Acomodado Pendiente de Paridad"
            if sge_funct.validar_po_status2(img_status, nombre_status_esperado):
                print("Cerrar sesion SGE")
                sge_funct.terminate_sge_session()
                # print(" Generando PO  PSC STATUS 10")
                # num_status = "10"
                ## paso el nombre completo de archivo txt para poder eliminarlo o mover el archivo y crear el nuevo
                # psc_number, psc_file_txt = sge_funct.crear_modificar_psc_status_xx(po_seleccionada, num_status)
                # print("mover el archivo PSC generado a carpeta de estatus correspondiente")
                # psc_generado_path = files.internacionales_tmp_psc_folder
                # psc_path_destino = files.internacionales_psc_status_10_folder
                # sge_funct.mover_po_internacionales(po_seleccionada, psc_generado_path, psc_path_destino)
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
                    # crear funcion para generar MUP
                    # generar archivo MUP EN CARPETA MUP
                    # pasar path MUP.txT
                    print("3 Ingresar archivo de Paridad CNP")
                    # CREAR FUNCION PARA SUBIR  Ingresar archivo de Paridad CNP
                    sge_funct.subir_po_sftp_internacional_por_psc_txt(files.base_Revisada_12_folder, psc_select_txt)
                    print("4 Press Enter Enter")
                    sge_funct.press_enter()
                    print("5 salir de sftp exit")
                    sge_funct.send_text("exit")
                    print("6 Press Enter Enter")
                    sge_funct.press_enter()
                    sge_funct.segundos_de_espera(2)
                    # ____________________________________________BLOQUE SGE ADM EJECUTAR JOB
                    print("7 iniciar sesion en SGE con usuario con permisos login_adm_sge")
                    sge_funct.sge_connection(login_data.adm_username, login_data.ip, login_data.adm_password)
                    print("8 Ejecutar JOB PARIDAD procesa_EDI.sh 'REC_PARIDAD'")
                    sge_funct.send_text("bash procesa_EDI.sh 'REC_PARIDAD'")
                    print("9 Press Enter Enter")
                    sge_funct.press_enter()
                    print("10 tiempo fuera 15 segundos")
                    sge_funct.segundos_de_espera(15)
                    # OBTENER CAPTURA JOB PARIDAD
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
                        print("1 Ingresar a SGE con las credenciales <<User>> <Password>>")
                        # conectado = sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial)
                        conectado = sge_funct.sge_connection(login_data.username, login_data.ip, login_data.password)

                        if conectado:
                            print("2 Press Enter Enter")
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
                            print("13,Situarse en la orden de compra e ingresar el numero de PO.")
                            # inv o num po?
                            sge_funct.send_text(inv_po_seleccionada)
                            print("14,Teclear input ,Enter")
                            sge_funct.press_enter()
                            print("15,Teclear input ,S")
                            sge_funct.send_text("S")
                            print("16,Teclear input ,Enter")
                            sge_funct.press_enter()
                            print("Copiar el numero de la PO presionando doble click izquierdo en el nombre de la PO doubleclick")
                            # double click obtener imagen si es necesario o send_text en el siguiente paso de ctrl+a
                            print("Presionar la combinacion de teclas: 'Ctrl + a'")
                            sge_funct.press_hotkeys("ctrl+a")
                            print("Situarse en la orden de compra e ingresar el numero de PO.")
                            sge_funct.send_text() #o rclick obtener coordenadas
                            print("16,Teclear input ,Enter")
                            sge_funct.press_enter()
                            print("15,Teclear input ,S")
                            sge_funct.send_text("S")
                            print("16,Teclear input ,Enter")

                            print("Validating Purchase Order")
                            nombre_status_esperado = "ACOMODADA PEND DE ENTR TE"
                            # OBTENER IMAGEN ACOMODADA PEND DE ENTR TE
                            img_status = images.img_status_en_transito
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
                                                                                                   nuevo_status,
                                                                                                   psc_select_txt)
                                print("MOVER el archivo PSC generado a carpeta de estatus correspondiente")

                                print(
                                    "REMOVE po PSC con status 10 de 'facturas_internacionales/revisada_en_origen_10'")
                                sge_funct.remove_file(files.internacionales_revisada_en_origen_10_folder,
                                                      psc_select_txt)
                                # eliminar factura en trasito utilizada en job?
                            else:
                                print("Fallo validacion, estatus Incorrecto")
                                assert False, "Fallo validacion, estatus Incorrecto"
                            # ____________________________________________BLOQUE SGE VALIDAR STATUS
        else:
            print(conectado)
            assert False, "Connection Failed!"



    def tearDown(self):
        sge_funct = sge_functions()
        sge_funct.terminate_sge_session()


if __name__ == '__main__':
    unittest.main()
