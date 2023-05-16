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
    def test_MTC_ASGE_021(self):

        #print("Test using: "+supplier)
        sge_funct = sge_functions2()
        print("------------------------------Pedimento Pagado Internacional")

        """TC21 ESTE TEST CASE NECESITA PO CON STATUS 'PEDIMENTO PAGADO (13)' """
        print("1 Ingresar a SGE con las credenciales <<User>> <Password>>")
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
                files.internacionales_pedimento_pagado_13_folder)
            # num_po
            sge_funct.send_text(num_po_seleccionada)
            print("14,Teclear input ,Enter")
            sge_funct.press_enter()
            print("15,Teclear input ,S")
            sge_funct.send_text("S")
            print("16,Teclear input ,Enter")
            sge_funct.press_enter()
            print("Validating Purchase Order")
            # --------------------borrar
            # print("17 Presionar la combinacion de teclas: 'Ctrl + a'  ctrl+a")
            # sge_funct.press_hotkeys("ctrl+a")
            # print("Situarse en la orden de compra e ingresar el numero de PO.")
            # # num_po
            # sge_funct.send_text(num_po_seleccionada)
            # print("16,Teclear input ,Enter")
            # sge_funct.press_enter()
            # print("15,Teclear input ,S")
            # sge_funct.send_text("S")
            # print("16,Teclear input ,Enter")

            # print("Validating Purchase Order")
            # nombre_status_esperado = "RECIBIDA POR AGTE AD"
            # #OBTENER IMAGEN
            # img_status = images.img_status_recibida_por_agte_ad
            # if sge_funct.validar_po_status2(img_status, nombre_status_esperado):
            #     print(f"Status {nombre_status_esperado} validado correctamente")
            #
            #     # eliminar PSC status 10
            #     print("eliminando psc procesada status 10...")
            #     path_archivo_origen = files.internacionales_revisada_en_origen_10_folder
            #     sge_funct.remove_file(path_archivo_origen, psc_select_txt)
            #
            #
            # else:
            #         print("Fallo validacion, estatus Incorrecto")
            #         assert False, "Fallo validacion, estatus Incorrecto"
            # # ____________________________________________BLOQUE SGE VALIDAR STATUS

            # --------------------borrar

            # CAMBIAR IMAGEN REVISADA POR AGTE AD
            img_status = images.img_status_revisada_por_agte_ad
            nombre_status_esperado = "REVISADA POR AGTE AD"
            if sge_funct.validar_po_status2(img_status, nombre_status_esperado):
                print("Cerrar sesion SGE")
                sge_funct.terminate_sge_session()

                print(" Generando PO  PSC STATUS 14")
                num_status = "14"
                path_destino = files.internacionales_en_proceso_de_cruce_14_folder
                psc_number, psc_file_txt = sge_funct.crear_modificar_psc_status_xx(num_po_seleccionada, path_destino,
                                                                                   num_status)

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
                    # cual es ese archivo?
                    print("3 Ingresar archivo de cambios de estatus PSC ESTATUS 14")
                    sge_funct.subir_po_sftp_internacional_por_psc_txt(files.internacionales_en_proceso_de_cruce_14_folder,
                                                                      psc_select_txt)
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
                    print("Ingresar archivo de cambios de estatus PSC ESTATUS 13")
                    print("8 Ejecutar JOB STATUS CHANGE bash procesa_EDI.sh REC_ESTATUS_TXT")
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

                        # copiar psc utilizada  en status 14 para reporte
                        path_archivo_destino = files.directory_tmp_file
                        sge_funct.copiar_po_internacionales(num_po_seleccionada,
                                                            files.internacionales_en_proceso_de_cruce_14_folder,
                                                            path_archivo_destino)

                        print("13 tiempo fuera 2 segundos")
                        sge_funct.segundos_de_espera(2)

                        # ____________________________________________BLOQUE SGE ADM EJECUTAR JOB

                        print("1 Ingresar a SGE con las credenciales <<User>> <Password>>")
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
                            # um po?
                            sge_funct.send_text(num_po_seleccionada)
                            print("14,Teclear input ,Enter")
                            sge_funct.press_enter()
                            print("15,Teclear input ,S")
                            sge_funct.send_text("S")
                            print("16,Teclear input ,Enter")
                            sge_funct.press_enter()
                            print("17 Presionar la combinacion de teclas: 'Ctrl + a'  ctrl+a")
                            sge_funct.press_hotkeys("ctrl+a")
                            print("Situarse en la orden de compra e ingresar el numero de PO.")
                            # num_po
                            sge_funct.send_text(num_po_seleccionada)
                            print("16,Teclear input ,Enter")
                            sge_funct.press_enter()
                            print("15,Teclear input ,S")
                            sge_funct.send_text("S")
                            print("16,Teclear input ,Enter")

                            print("Validating Purchase Order")
                            # nombre_status_esperado = "EN CRUCE POR AGTE AD"
                            # # OBTENER IMAGEN EN CRUCE POR AGTE AD
                            # img_status = images.img_status_pedimento_pagado
                            # if sge_funct.validar_po_status2(img_status, nombre_status_esperado):
                            #     print(f"Status {nombre_status_esperado} validado correctamente")
                            #     # eliminar PSC status 13
                            #     print("eliminando psc procesada status 13...")
                            #     path_archivo_origen = files.internacionales_pedimento_pagado_13_folder
                            #     sge_funct.remove_file(path_archivo_origen, psc_select_txt)


                        else:
                            print("Fallo validacion, estatus Incorrecto")
                            assert False, "Fallo validacion, estatus Incorrecto"
                        # ____________________________________________BLOQUE SGE VALIDAR STATUS
        else:
            print(conectado)
            assert conectado, "error de conexion"

    def tearDown(self):
        sge_funct = sge_functions2()
        # sge_funct.terminate_sge_session()

if __name__ == '__main__':
    unittest.main()

