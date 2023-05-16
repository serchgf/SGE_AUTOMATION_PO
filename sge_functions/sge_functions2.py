import random

from Config.config import txt_files_path
from Config.config import login_data
from Config.config import data_sftp_connection
from Config.config import files
from Config.config import commons_cmds
from Config.config import images
from Config.connections import sftp_connection
import os
import pyautogui as pa
import subprocess
import time
import datetime
import shutil
from pyperclip import paste
import csv
import pysftp


class sge_functions2:
    img_pantalla_inicial = images.img_pantalla_inicial
    img_error_connection = images.img_error_connection
    img_inicio_orden_de_compra = images.img_inicio_orden_de_compra
    img_consulta_orden_de_compra = images.img_consulta_orden_de_compra
    img_confirmacion_colocada = images.img_confirmacion_colocada
    img_header_orden_de_compra = images.img_header_orden_de_compra
    img_status_confirmada_por_proveedor = images.img_status_confirmada_por_proveedor
    img_sftp_connection_valid = images.img_sftp_connection_valid
    img_status_job_ok = images.img_status_job_ok
    img_status_job_pend = images.img_status_job_pend
    img_suc_xx = images.img_suc_xx

    #############
    img_promociones = images.img_promociones
    img_promociones2 = images.img_promociones2
    img_atraso = images.img_error_atraso_importante
    img_gdl = images.img_error_gdl
    #############

    # inv_base_text_file = files.inv_base_txt_file
    factura_valida_text_file = txt_files_path.fact_valida_txt_file
    factura_invalida_text_file = txt_files_path.fact_invalida_txt_file
    txt_psc_po_por_confirmar_internacional = txt_files_path.txt_psc_po_por_confirmar_internacional
    factura_internacional_valida = txt_files_path.fact_internacional_valida_txt
    factura_internacional_invalida = txt_files_path.fact_internacional_invalida_txt
    archivo_psc_base = txt_files_path.archivo_psc_base

    close_as = ""
    route_image = ""
    po_seleccionada = ""

    def create_report_directory(self):
        main_report_dir = 'Reports/SGE_PO_Test_report_' + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M/")
        """main_report_dir = 'images_report/SGE_PO_Test_report ' + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S/")"""
        return main_report_dir

    def sge_connection(self, username, ip, password):
        try:
            connect = 'putty.exe -ssh {}@{} -pw {}'.format(username, ip, password)
            subprocess.Popen(connect, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            time.sleep(3)
        except:
            print("Connection Failed...\nCheck your credentials access...")

    def validate_sge_connection(self):
        time.sleep(1)
        s = pa.locateOnScreen(self.img_pantalla_inicial)
        e = pa.locateOnScreen(self.img_error_connection)
        if s is not None:
            # print("Connection Successful!!")
            return True

        elif e is not None:
            time.sleep(1)
            message = "Connection Failed"
            self.take_screenshot(message)
            # print("Error Found, Connection Failed!!")
            return False, "Error Found, Connection Failed"
        else:
            assert False, "Error connection no defined"

    def press_general_commands(self, cmd, img_r_Click, img_doubleClick, archivo_productos):
        if cmd == commons_cmds.ctrlb:
            self.press_Test_hotkey(cmd)

        if cmd == commons_cmds.ctrle:
            pa.hotkey('ctrl', 'e')

        elif cmd == commons_cmds.ctrlw:
            pa.hotkey('ctrl', 'w')

        elif cmd == commons_cmds.ctrlr:
            pa.hotkey('ctrl', 'r')

        elif cmd == commons_cmds.ctrlo:
            pa.hotkey('ctrl', 'o')

        elif cmd == commons_cmds.ctrlk:
            pa.hotkey('ctrl', 'k')

        elif cmd == commons_cmds.arrow_down:
            pa.press('down')

        elif cmd == commons_cmds.ctrla:
            pa.hotkey('ctrl', 'a')

        elif cmd == commons_cmds.promociones:
            # pass
            while self.promociones_y_atrasos():
                pa.hotkey('ctrl', 'a')

        elif cmd == commons_cmds.validar_cdi:
            self.sugerencia_CEDI()

        elif cmd == commons_cmds.validar_job_ok:
            flag = self.validar_job_status_ok()
            if flag:
                print("Job Executed correctly...")
            else:
                print("Job status not expected...")
                message = "Job status not expected..."
                self.take_screenshot(message)
                pa.typewrite("exit")
                assert False, "Job status not expected..."

        elif cmd == commons_cmds.validar_job_pend:
            flag = self.validar_job_status_pend()
            if flag:
                print("Job status 'Pend' correctly...")
            else:
                print("Job status not expected...")
                message = "Job status not expected..."
                self.take_screenshot(message)
                pa.typewrite("exit")
                assert False, "Job status not expected..."


        elif cmd == commons_cmds.tab:
            # pa.press('tab')
            pa.hotkey(commons_cmds.tab)

        elif cmd == commons_cmds.space:
            pa.press('space')

        elif cmd == "leer_archivo" or cmd == "read_file":
            # pa.press('tab')
            # with open(txt_files_path.txt_file, 'r') as f1:
            with open(archivo_productos, 'r') as f1:
                for line in f1:
                    print(line)
                    pa.typewrite(line)
                # pa.press('tab')

        elif cmd == commons_cmds.doubleClick:
            time.sleep(5)
            img_coordinates = pa.locateCenterOnScreen(img_doubleClick)
            pos_x = img_coordinates[0]
            pos_y = img_coordinates[1]

            nueva_x = pos_x + 10
            pa.doubleClick(nueva_x, pos_y)

        elif cmd == commons_cmds.rclick:
            coordinates_rclick = pa.locateCenterOnScreen(img_r_Click)
            pa.click(coordinates_rclick, button="right")

        elif cmd == commons_cmds.subir_archivo:
            self.subir_archivo_sftp()

        elif cmd == commons_cmds.subir_fact_invalida:
            self.subir_factura_sftp()

        elif cmd == commons_cmds.enter:
            pa.press('enter')
            time.sleep(1)

        elif cmd == commons_cmds.pegar_num_inv_po:
            self.pegar_num_inv_po()

        elif cmd == commons_cmds.pegar_num_po:
            self.pegar_num_po()

        elif cmd == commons_cmds.login_sge:
            self.sge_connection(login_data.username, login_data.ip, login_data.password)
            time.sleep(1)

        elif cmd == commons_cmds.login_adm_sge:
            self.sge_connection(login_data.adm_username, login_data.ip, login_data.adm_password)
            time.sleep(1)

        elif cmd == commons_cmds.login_sftp:
            sftp_connection.sftp_connection(data_sftp_connection.sftp_hostname, data_sftp_connection.sftp_username,
                                            data_sftp_connection.sftp_hostname)
            time.sleep(1)

        elif "sucursal" in cmd:
            str_list = cmd.split()
            num_suc = str(str_list[1]).lstrip()
            pa.press(num_suc)
            time.sleep(1)
            self.validar_seleccion_sucursal(num_suc)



        elif cmd == commons_cmds.tiempo_fuera_2:
            time.sleep(2)

        elif cmd == commons_cmds.tiempo_fuera_3:
            time.sleep(3)

        elif cmd == commons_cmds.tiempo_fuera_5:
            time.sleep(5)

        elif cmd == commons_cmds.tiempo_fuera_10:
            time.sleep(10)

        elif cmd == commons_cmds.tiempo_fuera_20:
            time.sleep(20)
        else:
            self.type_cmds(cmd)



    def take_screenshot(self, message):
        print("taking screenshot " + message)
        img_name = f"my_screenshot.png"
        pa.screenshot(f"Screenshots/{img_name}")
        # return self.route_image

    def close_sge_session(self, close_as):
        pa.press('enter')
        pa.hotkey('alt', 'f4')
        if close_as != 0:
            pa.press('enter')
        else:
            pass

    def validating_po(self):
        time.sleep(1)
        try:
            coord_xy = pa.locateOnScreen(self.img_confirmacion_colocada)
            if coord_xy != "":
                print("PO Created successfully")
                message = "PO_successful"
                self.take_screenshot(message)
                # self.create_inv_txt_file()
                self.close_as = 0
                return True
        except:
            print("An error has occurred, PO no created")
            message = "Test_failed"
            time.sleep(1)
            self.take_screenshot(message)
            assert False, "An error has occurred, PO no created"

    def create_general_po(self, object_list_to_process, img_r_Click: None, img_doubleClick: None,
                          archivo_productos: None, fact_valida: None, fact_invalida: None):
        print("Creating general invoice")
        try:
            self.read_general_commands(object_list_to_process, img_r_Click, img_doubleClick, archivo_productos)
        except:
            print("An error has occurred, During Invoice creation")
            message = "Error_during_Invoice_Creation"
            time.sleep(1)
            self.take_screenshot(message)
            assert False, "An error has occurred, A command has not been processed correctly"

    def obtener_fecha(self):
        fecha = str(datetime.datetime.now())
        fecha = fecha.split(".")
        final = ""
        if ":" in fecha[0]:
            nueva = fecha[0].replace(":", "h_", 1)
            semi = nueva.replace(":", "min_", 2)
            final = semi + "s_"
            final = final.replace(" ", "_")
        return final

    def error_screenshot(self):
        message = "connection_error"
        self.take_screenshot(message)

    def terminate_sge_session(self):
        print("Test finished...")
        self.close_sge_session(self.close_as)
        print("Session terminated")

    def move_to_report_dir(self, img_to_move, path_to_move):
        # obtain name of directory
        #self.create_report_directory()
        # shutil.move(f"screenshots/funcionaScreenshot.png", f"{path_to_move}/{img_to_move}")
        try:
            shutil.move(f"screenshots/my_screenshot.png", f"{path_to_move}/{img_to_move}")
            file_source = files.directory_tmp_file
            file_destination = path_to_move
            copy_file_destination = files.valid_inv_confirmed_po_file
            get_files = os.listdir(file_source)
            for f in get_files:
                try:
                    #shutil.copy(file_source + f, copy_file_destination + f)
                    shutil.move(file_source + f, file_destination + f)
                except:
                    print("Error, INV file no Generated")
        except:
            shutil.copy(f"image_files/oops.png", f"{path_to_move}/{img_to_move}")

        return f"images_report/{img_to_move}"

    def promociones_y_atrasos(self):

        gdl = pa.locateOnScreen(self.img_gdl)
        atraso = pa.locateOnScreen(self.img_atraso)
        p2 = pa.locateOnScreen(self.img_promociones2)
        p = pa.locateOnScreen(self.img_promociones)
        if atraso is not None or p is not None or p2 is not None or gdl is not None:
            return True
        else:
            return False

    def sugerencia_CEDI(self):
        time.sleep(2)
        gdl = pa.locateOnScreen(self.img_gdl)
        if gdl is not None:
            pa.press('s')

    # functions to create the new inv text file

    def create_inv_txt_file(self):
        headerOrdencompra = pa.locateCenterOnScreen(self.img_header_orden_de_compra)
        if headerOrdencompra != "":
            # print("-----------------------------")
            # print("encontrado")
            # print(headerOrdencompra)
            pos_x = headerOrdencompra[0]
            pos_y = headerOrdencompra[1]
            nueva_y = pos_y + 35
            pa.doubleClick(pos_x, nueva_y)
            # print("NNNNNNNNNNNNNNNNNNNNNNNNNOMBREE")
            nombre_po = str(paste())
            pa.click(pos_x, nueva_y)
            print(f"numero PO: {nombre_po}")
            output_txt_file = f"{files.directory_tmp_file}INV-{nombre_po}.txt"
            # ---------------------------------- inicio creando archivo factura valida
            with open(self.factura_valida_text_file) as file, open(output_txt_file, "w") as output:
                # with open(invoice_txt) as file, open(output_txt_file, "w") as output:
                for index, line in enumerate(file):
                    # output.write(line)
                    if index == 1:
                        line_1 = line.split("|")
                        new_line_1 = self.replace_list_index_1(line_1, nombre_po)
                        output.write(new_line_1)
                        # fyl.write(str(paste()), '\n')
                    else:
                        output.write(line)
            # ---------------------------------- fin creando archivo factura valida
            #####################################
            # ---------------------------------- inicio creando archivo factura INVALIDA
            output_txt_file = f"{files.invalid_inv_folder}INV-{nombre_po}.txt"
            with open(self.factura_invalida_text_file) as file, open(output_txt_file, "w") as output:
                # with open(invoice_txt) as file, open(output_txt_file, "w") as output:
                for index, line in enumerate(file):
                    # output.write(line)
                    if index == 1:
                        line_1 = line.split("|")
                        new_line_1 = self.replace_list_index_1(line_1, nombre_po)
                        output.write(new_line_1)
                        # fyl.write(str(paste()), '\n')
                    else:
                        output.write(line)
            # ---------------------------------- fin creando archivo factura INVALIDA
        else:
            print("header no encontrado")
            print(headerOrdencompra)
        # return output_txt_file

    def replace_list_index_1(self, lista_a, nombre_po):

        nspacesl_0 = 25 - len(nombre_po)
        nspacesl_1 = 25 - len("INV" + nombre_po)

        lista_a[0] = nombre_po + " " * nspacesl_0
        lista_a[1] = "INV" + nombre_po + " " * nspacesl_1
        # campo Fecha
        lista_a[3] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S'")

        # print("modificado")
        nl = []
        for i in lista_a:
            if i != lista_a[-1]:
                i = i + "|"
            nl.append(i)
        return "".join(map(str, nl))

    def replace_list_index_internacional_num_po_datetime(self, lista_a, nombre_po):
        """
        regresa linea 1 del archivo con nuevas modificaciones
        :param lista_a:
        :param nombre_po:
        :param status_colocada:
        :return: nombre modificado, hora y fecha modificada
        """
        nspacesl_0 = 25 - len(nombre_po)
        nspacesl_7 = 25 - len(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


        lista_a[0]= nombre_po+ " "*nspacesl_0
        #lista_a[1] = "INV"+nombre_po +" "*nspacesl_1
        lista_a[7] = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{' '*nspacesl_7}"

        nl= []
        for i in lista_a:
            if i != lista_a[-1]:
                i = i+"|"
            nl.append(i)
        return "".join(map(str,nl))

    def replace_psc_num_po_and_status(self, lista_a, nombre_po, num_status):
        """
        :param lista_a: lista de linea[1] del archivo que se modificara
        :param nombre_po: str nuevo nombre
        :param num_status: str nuevo status
        :return: string linea 1 con nuevo_nombre_po, nuevo_inv, nuevo_status, nueva_datetime
        """
        nspacesl_0 = 25 - len(nombre_po)
        nspacesl_1 = 25 - len("INV" + nombre_po)
        nspacesl_3 = 2 - len(num_status)
        # num po
        lista_a[0] = nombre_po + " " * nspacesl_0
        # num inv
        lista_a[1] = "INV" + nombre_po + " " * nspacesl_1
        # status id
        lista_a[3] = num_status + " " * nspacesl_3

        #se modifica fecha tambien?
        # print("modificado")
        nl = []
        for i in lista_a:
            if i != lista_a[-1]:
                i = i + "|"
            nl.append(i)
        return "".join(map(str, nl))


    def replace_MUP_(self, lista_a, nombre_po):
        """
        modificara los campos indicados del archivo MUP
        :param lista_a:
        :param nombre_po:
        :return:
        """

        # nspacesl_0 = 25 - len(nombre_po)
        # nspacesl_1 = 25 - len("INV" + nombre_po)
        # nspacesl_3 = 2 - len(num_status)
        # # num po
        # lista_a[0] = nombre_po + " " * nspacesl_0
        # # num inv
        # lista_a[1] = "INV" + nombre_po + " " * nspacesl_1
        # # status id
        # lista_a[3] = num_status + " " * nspacesl_3
        #
        # #se modifica fecha tambien?
        # # print("modificado")
        # nl = []
        # for i in lista_a:
        #     if i != lista_a[-1]:
        #         i = i + "|"
        #     nl.append(i)
        # return "".join(map(str, nl))


    def replace_psc_name_inv_status_time(self, lista_a, nombre_po, num_status):
        """
        :param lista_a: lista de linea[1] del archivo que se modificara
        :param nombre_po: str nuevo nombre
        :param num_status: str nuevo status
        :return: string linea 1 con nuevo_nombre_po, nuevo_inv, nuevo_status, nueva_datetime
        """
        #btener numero de espacios en blanco de cada campo
        nspacesl_0 = 25 - len(nombre_po)
        nspacesl_1 = 25 - len("INV" + nombre_po)
        nspacesl_3 = 2 - len(num_status)
        nspacesl_7 = 25 - len(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # num po
        lista_a[0] = nombre_po + " " * nspacesl_0
        # num inv
        lista_a[1] = "INV" + nombre_po + " " * nspacesl_1
        # status id
        lista_a[3] = num_status + " " * nspacesl_3
        # date time
        lista_a[7] = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{' '*nspacesl_7}"

        #se modifica fecha tambien?
        # print("modificado")
        nl = []
        for i in lista_a:
            if i != lista_a[-1]:
                i = i + "|"
            nl.append(i)
        return "".join(map(str, nl))

    def validado_por_proveedor(self):
        time.sleep(1)
        try:
            coord_xy = pa.locateOnScreen(self.img_status_confirmada_por_proveedor)
            # print("6666666666666666666666666666666666666666666666666")
            # print(coord_xy)
            if coord_xy != "":
                print("PO validated successfully")
                message = "PO_validated_successful"
                self.take_screenshot(message)
                self.create_inv_txt_file()
                self.close_as = 0
                return True
            else:
                return False
        except:
            print("An error has occurred, PO no validated")
            message = "Test_failed"
            time.sleep(1)
            self.take_screenshot(message)
            assert False, "An error has occurred, PO no validated"

    def validar_status_post_job(self, img_status):
        time.sleep(1)
        try:
            coord_xy = pa.locateOnScreen(img_status)
            # print("6666666666666666666666666666666666666666666666666")
            # print(coord_xy)
            if coord_xy != "":
                print("Status validated successfully")
                message = "PO_status_validated_successful"
                self.take_screenshot(message)
                self.create_inv_txt_file()
                self.close_as = 0
                return True
            else:
                return False
        except:
            print("An error has occurred, PO status not expected")
            message = "Test_failed"
            time.sleep(1)
            self.take_screenshot(message)
            assert False, "An error has occurred, PO status not expected"

    def pegar_num_inv_po(self):
        print(f"pegando numero numero de INV: {self.po_seleccionada}")
        pa.typewrite(f"INV{self.po_seleccionada}")

    def pegar_num_po(self):
        print(f"pegando numero numero de PO: {self.po_seleccionada}")
        pa.typewrite(f"{self.po_seleccionada}")

    def validar_po_status(self, img_status_po, nombre_status):
        time.sleep(1)
        print(f"Validating PO Status...{nombre_status}")
        in_screen = pa.locateOnScreen(img_status_po)
        if in_screen != '' or in_screen != None:
            print(in_screen)
            print(f"PO Status {nombre_status} Correct...")
            message = (f"PO Status {nombre_status} Correct")
            self.take_screenshot(message)
            # print(f"copiando factura con status: {nombre_status} a /facturas_generadas/... ")
            #

            # mover factura valida mover a procesados
            #shutil.move(f"{files.valid_inv_confirmed_po_file}INV-{self.po_seleccionada}.txt",
            #            f"{files.processed_inv_file}INV-{self.po_seleccionada}.txt")

            # mover factura invalida mover a procesados con renombre invalida
            #shutil.move(f"{files.invalid_inv_folder}INV-{self.po_seleccionada}.txt",
            #            f"{files.processed_inv_file}INV-{self.po_seleccionada}INVALIDA.txt")
            return True
        else:
            print("PO status not expected...")
            message = ("PO status not expected...")
            self.take_screenshot(message)
            # mover factura valida mover a procesados
            shutil.move(f"{files.valid_inv_confirmed_po_file}INV-{self.po_seleccionada}.txt",
                        f"{files.processed_inv_file}INV-{self.po_seleccionada}.txt")
            # mover factura invalida mover a procesados con renombre invalida
            shutil.move(f"{files.invalid_inv_folder}INV-{self.po_seleccionada}.txt",
                        f"{files.processed_inv_file}INV-{self.po_seleccionada}INVALIDA.txt")
            return False

    def mover_factura_status_en_trasito_a_recibida_en_proceso_de_revision(self, num_po_seleccionada):
        try:
            shutil.move(f"{files.inv_en_transito_folder}INV-{num_po_seleccionada}.txt",
                        f"{files.inv_recibida_en_revision_folder}INV-{num_po_seleccionada}.txt")
        except:
            print("no se movio el archivo")

    def mover_factura_status_recibida_en_proceso_de_revision_a_proceso_Acomodo_Nacional(self, num_po_seleccionada):
        try:
            shutil.move(f"{files.inv_recibida_en_revision_folder}INV-{num_po_seleccionada}.txt",
                        f"{files.inv_en_proceso_de_acomodo_folder}INV-{num_po_seleccionada}.txt")
        except:
            print("no se movio el archivo")

    def mover_facturas(self, num_po_seleccionada: str, path_directorio_origen: str, path_directorio_destino: str):
        try:
            shutil.move(f"{path_directorio_origen}INV-{num_po_seleccionada}.txt",
                        f"{path_directorio_destino}INV-{num_po_seleccionada}.txt")
        except:
            print("no se movio el archivo")

    def copiar_facturas(self, num_po_seleccionada: str, path_directorio_origen: str, path_directorio_destino: str):
        try:
            shutil.copy(f"{path_directorio_origen}INV-{num_po_seleccionada}.txt",
                        f"{path_directorio_destino}INV-{num_po_seleccionada}.txt")
        except:
            print("no se movio el archivo")

    def copiar_po_internacionales(self, num_po_seleccionada: str, path_directorio_origen: str, path_directorio_destino: str):
        """

        :param num_po_seleccionada:
        :param path_directorio_origen:
        :param path_directorio_destino:
        :return:
        """
        try:
            shutil.copy(f"{path_directorio_origen}PSC-{num_po_seleccionada}-10052023-172258.txt",
                        f"{path_directorio_destino}PSC-{num_po_seleccionada}-10052023-172258.txt")
        except:
            print("no se copio el archivo")



    def mover_po_internacionales(self, num_po_seleccionada: str, path_directorio_origen: str, path_directorio_destino: str):
        try:
            shutil.move(f"{path_directorio_origen}PSC-{num_po_seleccionada}-10052023-172258.txt",
                        f"{path_directorio_destino}PSC-{num_po_seleccionada}-10052023-172258.txt")
        except:
            print("no se movio el archivo")


    def validar_seleccion_sucursal(self, n_sucursal):
        num_sucursal = images.img_suc_xx.replace("xx", n_sucursal)
        time.sleep(1)
        print(f"la sucursal elegida es : {n_sucursal}")
        try:
            coord_xy = pa.locateOnScreen(num_sucursal)
            print(f"las coordenadas son: {coord_xy}")
            if coord_xy != "":
                print("Sucursal seleccionada correctamente")
                return True
            else:
                print("Error, Sucursal no seleccionada, Reintentando...")
                return False
        except:
            print("EXCEPT Error, Sucursal no seleccionada...")

    # ----------------------------------------------------------------------------SFTP
    def sftp_connection(self):
        sftp_con = sftp_connection()
        sftp_con.sftp_connection(data_sftp_connection.sftp_hostname, data_sftp_connection.sftp_username,
                                 data_sftp_connection.sftp_password)

    def validate_sftp_connection(self):
        time.sleep(1)
        in_sftp = pa.locateOnScreen(self.img_sftp_connection_valid)
        if in_sftp != '' or in_sftp != None:
            print(in_sftp)
            print("SFTP Connection established...")
            return True
        else:
            print("Connection Failed...\nCheck your credentials access...")
            return False

    def subir_archivo_sftp(self):
        """ cmd debe ser la ruta en el servidor donde se subira el archivo"""
        file_source = files.valid_inv_confirmed_po_file
        get_files = os.listdir(file_source)
        random_inv = random.choice(get_files)
        print(f"INV seleccionada: {random_inv}")
        pa.typewrite(f"put {file_source + random_inv}")
        # pa.press('enter')
        self.po_seleccionada = str(random_inv).replace("INV-", "").replace(".txt", "")
        return self.po_seleccionada

    def subir_factura_sftp(self, path_origen):
        """ cmd debe ser la ruta en el servidor donde se subira el archivo"""
        file_source = path_origen
        get_files = os.listdir(file_source)
        random_inv = random.choice(get_files)
        print(f"INV seleccionada: {random_inv}")
        pa.typewrite(f"put {file_source + random_inv}")
        # pa.press('enter')
        num_po_seleccionada = str(random_inv).replace("INV-", "").replace(".txt", "")
        inv_po_seleccionada = str(random_inv).replace("-", "").replace(".txt", "")
        return num_po_seleccionada, inv_po_seleccionada

    def validar_job_status_ok(self):
        time.sleep(2)
        print("Validating job Status...")
        in_sftp = pa.locateOnScreen(self.img_sftp_connection_valid)
        if in_sftp != '' or in_sftp is not None:
            # n_sftp != '' or in_sftp != None:
            print(in_sftp)
            return True
        else:
            print("Job status not expected...")
            return False

    def validar_job_status_pend(self):
        time.sleep(2)
        print("Validating job Status...")
        in_sftp = pa.locateOnScreen(self.img_status_job_pend)
        if in_sftp != '' or in_sftp is not None:
            # n_sftp != '' or in_sftp != None:
            print(in_sftp)
            return True
        else:
            print("Job status not expected...")
            return False

    # ----------------------------------------------------------------------------SFTP

    def login_adm_sge(self, adm_username: str, ip: str, adm_password: str):
        self.sge_connection(adm_username, ip, adm_password)
        time.sleep(2)
        self.send_text("cd automation")
        self.press_enter()
        self.send_text("principaluat02")
        self.press_enter()
        # Menu de sucursales
        time.sleep(1)

    def press_enter(self):
        pa.press('enter')
        time.sleep(1)

    def press_tab(self):
        pa.press('tab')
        time.sleep(1)

    def press_key(self, key_name: str):
        pa.press(key_name)
        time.sleep(1)

    def press_hotkeys(self, hot_key: str):
        hot_key = hot_key.split("+")
        pa.hotkey(hot_key[0].strip(), hot_key[1].strip())

    def send_text(self, my_text: str):
        pa.typewrite(my_text)
        time.sleep(1)

    def segundos_de_espera(self, x_segundos: int):
        time.sleep(x_segundos)

    def obtener_factura_en_transito(self):
        """ cmd debe ser la ruta en el servidor donde se subira el archivo"""
        # cambiar por direcrorio de facturas en transito
        file_source = files.inv_en_transito_folder
        get_files = os.listdir(file_source)
        # obteniendo una factura random
        random_inv = random.choice(get_files)
        # imprimir la factura seleccionada i.e INV-012M0021200282RD.txt
        print(f"INV seleccionada: {random_inv}")
        # guardando en una variable global solo el numero de la po, se elimina inv y .txt
        self.po_seleccionada = str(random_inv).replace("INV-", "").replace(".txt", "")
        num_po_seleccionada = self.po_seleccionada
        inv_po_seleccionada = str(random_inv).replace("-", "").replace(".txt", "")
        return num_po_seleccionada, inv_po_seleccionada


    def obtener_factura_de_directorio(self, path_factura_origen: str):

        file_source = path_factura_origen
        get_files = os.listdir(file_source)
        # obteniendo una factura random
        random_inv = random.choice(get_files)
        # imprimir la factura seleccionada i.e INV-012M0021200282RD.txt
        print(f"INV seleccionada: {random_inv}")
        # guardando en una variable global solo el numero de la po, se elimina inv y .txt
        self.po_seleccionada = str(random_inv).replace("INV-", "").replace(".txt", "")
        num_po_seleccionada = self.po_seleccionada
        inv_po_seleccionada = str(random_inv).replace("-", "").replace(".txt", "")
        return num_po_seleccionada, inv_po_seleccionada, random_inv

    def obtener_factura_de_directorio_internacional(self, path_factura_origen: str):

        file_source = path_factura_origen
        get_files = os.listdir(file_source)
        # obteniendo una factura random
        random_po = random.choice(get_files)
        # imprimir la po internacional seleccionada i.e PSC-012A002120032236-10052023-172258.txt
        print(f"INV seleccionada: {random_po}")
        # guardando en una variable global solo el numero de la po, se elimina inv y .txt
        po_internacional_seleccionada = str(random_po).replace('PSC-', '').replace('-10052023-172258.txt', '')
        inv_po_seleccionada = str(random_po).replace("PSC-", "INV").replace('-10052023-172258.txt', '')
        return po_internacional_seleccionada, inv_po_seleccionada, random_po

    def obtener_datos_psc_file(self, path_psc_origen: str):
        file_source = path_psc_origen
        get_files = os.listdir(file_source)
        # obteniendo una factura random
        random_psc_file = random.choice(get_files)
        # imprimir la po internacional seleccionada i.e PSC-012A002120032236-10052023-172258.txt
        print(f"PSC Seleccioando: {random_psc_file}")
        # guardando en una variable global solo el numero de la po, se elimina inv y .txt
        num_psc_seleccionada = str(random_psc_file).replace('PSC-', '').replace('-10052023-172258.txt', '')
        inv_psc_seleccionada = str(random_psc_file).replace("PSC-", "INV").replace('-10052023-172258.txt', '')
        return num_psc_seleccionada, inv_psc_seleccionada, random_psc_file


    def obtener_factura_en_proceso_de_revision(self):
        """ cmd debe ser la ruta en el servidor donde se subira el archivo"""
        # cambiar por direcrorio de facturas en transito
        file_source = files.inv_recibida_en_revision_folder
        get_files = os.listdir(file_source)
        # obteniendo una factura random
        random_inv = random.choice(get_files)
        # imprimir la factura seleccionada i.e INV-012M0021200282RD.txt
        print(f"INV seleccionada: {random_inv}")
        # guardando en una variable global solo el numero de la po, se elimina inv y .txt
        self.po_seleccionada = str(random_inv).replace("INV-", "").replace(".txt", "")
        num_po_seleccionada = self.po_seleccionada
        inv_po_seleccionada = str(random_inv).replace("-", "").replace(".txt", "")
        return num_po_seleccionada, inv_po_seleccionada



    def obtener_factura_confirmada_valida(self):
        pass

    def obtener_factura_invalida(self):
        pass

    def validate_adm_sge_connection(self, img_to_validate):
        time.sleep(1)
        s = pa.locateOnScreen(img_to_validate)

        if s is not None:
            # print("Connection Successful!!")
            return True
        else:
            assert False, "Error connection no defined"

    def validar_po_status2(self, img_status_po, nombre_status):
        time.sleep(1)
        print(f"Validating PO Status...{nombre_status}")
        in_screen = pa.locateOnScreen(img_status_po)
        if in_screen != '' or in_screen is not None:
            print(in_screen)
            print(f"PO Status {nombre_status} Correct...")
            message = ("PO Status {nombre_status} Correct")
            self.take_screenshot(message)
            return True

        else:
            print("PO status not expected...")
            message = ("PO status not expected...")
            self.take_screenshot(message)
            return False

    def leer_archivo_productos(self, archivo_productos):
        with open(archivo_productos, 'r') as f1:
            for line in f1:
                print(line)
                pa.typewrite(line)

    def doubleClick(self, img_doubleClick):
        time.sleep(3)
        img_coordinates = pa.locateCenterOnScreen(img_doubleClick)
        pos_x = img_coordinates[0]
        pos_y = img_coordinates[1]
        nueva_x = pos_x + 10
        pa.doubleClick(nueva_x, pos_y)

    def rightClick(self, img_r_Click):
        coordinates_rclick = pa.locateCenterOnScreen(img_r_Click)
        pa.click(coordinates_rclick, button="right")


    def re_validate_status(self, img_status):
        time.sleep(1)
        try:
            coord_xy = pa.locateOnScreen(img_status)
            #print("6666666666666666666666666666666666666666666666666")
            #print(coord_xy)
            if coord_xy != "":
                print("PO validated successfully")
                message = "PO_validated_successful"
                self.take_screenshot(message)
                self.create_inv_txt_file()
                self.close_as = 0
                return True
            else:
                return False
        except:
            print("An error has occurred, PO no validated")
            message = "Test_failed"
            time.sleep(1)
            self.take_screenshot(message)
            assert False, "An error has occurred, PO no validated"


    def crear_factura_valida_e_invalida_txt(self):
        headerOrdencompra = pa.locateCenterOnScreen(self.img_header_orden_de_compra)
        if headerOrdencompra != "":
            # print("-----------------------------")
            # print("encontrado")
            # print(headerOrdencompra)
            pos_x = headerOrdencompra[0]
            pos_y = headerOrdencompra[1]
            nueva_y = pos_y + 35
            pa.doubleClick(pos_x, nueva_y)
            # print("NNNNNNNNNNNNNNNNNNNNNNNNNOMBREE")
            nombre_po = str(paste())
            pa.click(pos_x, nueva_y)
            print(f"numero PO: {nombre_po}")
            output_txt_file_valid = f"{files.directory_tmp_file}INV-{nombre_po}.txt"
            # ---------------------------------- inicio creando archivo factura valida
            with open(self.factura_valida_text_file) as file, open(output_txt_file_valid, "w") as output:
                # with open(invoice_txt) as file, open(output_txt_file, "w") as output:
                for index, line in enumerate(file):
                    # output.write(line)
                    if index == 1:
                        line_1 = line.split("|")
                        new_line_1 = self.replace_list_index_1(line_1, nombre_po)
                        output.write(new_line_1)
                        # fyl.write(str(paste()), '\n')
                    else:
                        output.write(line)
            print(f"factura: INV{nombre_po}")
            # ---------------------------------- fin creando archivo factura valida
            shutil.copy(output_txt_file_valid, files.inv_confirmadas_validas_folder)
            #####################################
            # ---------------------------------- inicio creando archivo factura INVALIDA
            output_txt_file_invalid = f"{files.invalid_inv_folder}INV-{nombre_po}.txt"
            with open(self.factura_invalida_text_file) as file, open(output_txt_file_invalid, "w") as output:
                # with open(invoice_txt) as file, open(output_txt_file, "w") as output:
                for index, line in enumerate(file):
                    # output.write(line)
                    if index == 1:
                        line_1 = line.split("|")
                        new_line_1 = self.replace_list_index_1(line_1, nombre_po)
                        output.write(new_line_1)
                        # fyl.write(str(paste()), '\n')
                    else:
                        output.write(line)
            shutil.copy(output_txt_file_invalid, files.inv_invalidas_folder)
            # ---------------------------------- fin creando archivo factura INVALIDA
        else:
            print("header no encontrado")
            print(headerOrdencompra)
        # return output_txt_file

    def crear_archivo_po_por_confirmar_03_internacional_txt(self):
        headerOrdencompra = pa.locateCenterOnScreen(self.img_header_orden_de_compra)
        status_colocada = True
        if headerOrdencompra != "":

            pos_x = headerOrdencompra[0]
            pos_y = headerOrdencompra[1]
            nueva_y = pos_y + 35
            pa.doubleClick(pos_x, nueva_y)
            nombre_po = str(paste())
            pa.click(pos_x, nueva_y)
            print(f"numero PO: {nombre_po}")
            output_txt_file_valid = f"{files.directory_tmp_file}PSC-{nombre_po}-10052023-172258.txt"
            # ---------------------------------- inicio creando archivo factura valida
            with open(self.txt_psc_po_por_confirmar_internacional) as file, open(output_txt_file_valid, "w") as output:
                # with open(invoice_txt) as file, open(output_txt_file, "w") as output:
                for index, line in enumerate(file):
                    # output.write(line)
                    if index == 1:
                        line_1 = line.split("|")
                        new_line_1 = self.replace_list_index_internacional_num_po_datetime(line_1, nombre_po)
                        output.write(new_line_1)
                        # fyl.write(str(paste()), '\n')
                        output.write('\n')
                    else:
                        output.write(line)
            print(f"PO colocada por confirmar: {nombre_po}")
            return nombre_po

    def subir_archivo_sftp2(self, file_source):
        """ cmd debe ser la ruta en el servidor donde se subira el archivo"""
        get_files = os.listdir(file_source)
        random_inv = random.choice(get_files)
        print(f"INV seleccionada: {random_inv}")
        pa.typewrite(f"put {file_source + random_inv}")
        # pa.press('enter')
        self.po_seleccionada = str(random_inv).replace("INV-", "").replace(".txt", "")
        inv_po_seleccionada = str(random_inv).replace("-", "").replace(".txt", "")
        return self.po_seleccionada, inv_po_seleccionada, random_inv

    def subir_po_sftp_internacional(self, file_source):
        """ cmd debe ser la ruta en el servidor donde se subira el archivo"""
        get_files = os.listdir(file_source)
        random_po_txt = random.choice(get_files)
        num_po_seleccionada = str(random_po_txt).replace("PSC-", "").replace("-10052023-172258.txt", "")
        pa.typewrite(f"put {file_source + random_po_txt}")
        # pa.press('enter')

        inv_po_seleccionada = str(random_po_txt).replace("-", "").replace(".txt", "")
        return num_po_seleccionada, inv_po_seleccionada, random_po_txt

    def subir_po_sftp_internacional_por_psc_txt(self, path_origen, psc_txt):
        """ cmd debe ser la ruta en el servidor donde se subira el archivo"""

        print(f"PO internacional seleccionada: {psc_txt}")
        pa.typewrite(f"put {path_origen + psc_txt}")

        # pa.press('enter')

    def validar_job_status_x(self, img_status):
        time.sleep(2)
        print("Validating job Status...")
        in_sftp = pa.locateOnScreen(img_status)
        if in_sftp != '' or in_sftp is not None:
            # n_sftp != '' or in_sftp != None:
            print(in_sftp)
            return True
        else:
            print("Job status not expected...")
            message = "Job status not expected"
            self.take_screenshot(message)
            return False


    def crear_factura_valida_e_invalida_internacional_txt(self, nombre_po):

        print(f"numero PO: {nombre_po}")
        output_txt_file_valid = f"{files.directory_tmp_file}INV-{nombre_po}.txt"
        # ---------------------------------- inicio creando archivo factura valida
        with open(self.factura_internacional_valida) as file, open(output_txt_file_valid, "w") as output:
            # with open(invoice_txt) as file, open(output_txt_file, "w") as output:
            for index, line in enumerate(file):
                # output.write(line)
                if index == 1:
                    line_1 = line.split("|")
                    new_line_1 = self.replace_list_index_1(line_1, nombre_po)
                    output.write(new_line_1)
                    # fyl.write(str(paste()), '\n')
                else:
                    output.write(line)
        print(f"factura: INV{nombre_po}")
        # ---------------------------------- fin creando archivo factura valida
        shutil.copy(output_txt_file_valid, files.internacionales_inv_valida_folder)
        #####################################
        # ---------------------------------- inicio creando archivo factura INVALIDA
        output_txt_file_invalid = f"{files.internacionales_inv_invalida_folder}INV-{nombre_po}.txt"
        with open(self.factura_internacional_invalida) as file, open(output_txt_file_invalid, "w") as output:
            # with open(invoice_txt) as file, open(output_txt_file, "w") as output:
            for index, line in enumerate(file):
                # output.write(line)
                if index == 1:
                    line_1 = line.split("|")
                    new_line_1 = self.replace_list_index_1(line_1, nombre_po)
                    output.write(new_line_1)
                    # fyl.write(str(paste()), '\n')
                else:
                    output.write(line)
        # ---------------------------------- fin creando archivo factura INVALIDA

    def crear_modificar_psc_status_xx(self, numero_po, path_destino, num_status_nuevo):
        # o debe tener el que ya llevo desde el inicio PSC-num_po-10052023-172258
        archivo_psc_base_path = self.archivo_psc_base
        archivo_psc_base_name = txt_files_path.archivo_psc_base_name
        print(f"numero PO: {numero_po}")
        output_psc_file_txt_name = archivo_psc_base_name.replace('num_po', numero_po)
        # ---------------------------------- inicio creando archivo factura valida
        with open(archivo_psc_base_path) as file, open(path_destino+output_psc_file_txt_name, "w") as output:
            # with open(invoice_txt) as file, open(output_txt_file, "w") as output:
            for index, line in enumerate(file):
                # output.write(line)
                if index == 1:
                    line_1 = line.split("|")
                    new_line_1 = self.replace_psc_name_inv_status_time(line_1, numero_po, num_status_nuevo)
                    output.write(new_line_1)
                    output.write('\n')
                    # fyl.write(str(paste()), '\n')
                else:
                    output.write(line)

        psc_number = output_psc_file_txt_name.replace('.txt', '')
        print(f"PSC Modificado: {psc_number}")
        print(f"PSC CREADO, STATUS ACTUALIZADO A: {num_status_nuevo}")
        psc_file_txt = output_psc_file_txt_name
        return psc_number, psc_file_txt

    def remove_file(self, psc_path_origen, file_name):
        """
        elimina archivo si proporcionas el directorio origen y el nombre del archivo
        :param psc_path_origen:
        :param file_name:
        :return:
        """
        if os.path.exists(psc_path_origen):
            os.remove(f"{psc_path_origen}{file_name}")
        else:
            print("The file does not exist")

    def remove_file2(self, psc_path_origen):
        """
        elimina el archivo proporcionando la ruta completa del archivo
        :param psc_path_origen:
        :return:
        """
        if os.path.exists(psc_path_origen):
            os.remove(psc_path_origen)
        else:
            print("The file does not exist")


    def crear_nombre_po_txt_tmp(self, numero_po):
        # ---------------------------------- inicio creando archivo factura valida
        output_path = files.internacionales_tmp_psc_folder
        file_name = f"{numero_po}.txt"
        with open(output_path+file_name, "w") as output:
            output.write(numero_po)

    def crear_archivo_status_13(self, num_po_txt_tmp):
        pass

    def crear_archivo_status_14(self, num_po_txt_tmp):
        pass

    def crear_archivo_status_15(self, num_po_txt_tmp):
        pass

    def crear_archivo_status_16(self, num_po_txt_tmp):
        pass

    def crear_archivo_status_17(self, num_po_txt_tmp):
        pass

    def crear_archivo_status_18(self, num_po_txt_tmp):
        pass

    def crear_archivo_status_19(self, num_po_txt_tmp):
        pass

    def crear_archivo_status_10(self, num_po_txt_tmp):
        # o debe tener el que ya llevo desde el inicio PSC-012A002120032236-10052023-172258
        archivo_psc_base = txt_files_path.Revisada_Origen_10_txt
        print(f"numero PO: {num_po_txt_tmp}")
        output_psc_file_txt_name = archivo_psc_base.replace('num_po', num_po_txt_tmp)
        psc_status_10 = files.internacionales_psc_status_10_folder
        if not os.path.exists(psc_status_10):
            os.makedirs(psc_status_10)

        # ---------------------------------- inicio creando archivo factura valida
        with open(archivo_psc_base) as file, open(psc_status_10+output_psc_file_txt_name, "w") as output:
            # with open(invoice_txt) as file, open(output_txt_file, "w") as output:
            for index, line in enumerate(file):
                # output.write(line)
                if index == 1:
                    line_1 = line.split("|")
                    new_line_1 = self.replace_psc_num_po_and_status(line_1, num_po_txt_tmp, "10")
                    output.write(new_line_1)
                    output.write('\n')
                    # fyl.write(str(paste()), '\n')
                else:
                    output.write(line)

        output_path_psc_txt_file = f"{files.internacionales_tmp_psc_folder}{output_psc_file_txt_name}"
        psc_number = output_psc_file_txt_name.replace('.txt', '')
        print(f"PSC: {psc_number}")
        print(f"PSC CREADO, STATUS ACTUALIZADO A: 10")
        psc_file_txt = output_psc_file_txt_name
        return psc_number, psc_file_txt


    def modificar_MUP(self, num_po: str):
        # o debe tener el que ya llevo desde el inicio PSC-012A002120032236-10052023-172258
        archivo_MUP_base = txt_files_path.Revisada_Origen_10_txt
        # print(f"numero PO: {num_po_txt_tmp}")
        # output_psc_file_txt_name = archivo_psc_base.replace('num_po', num_po_txt_tmp)
        # psc_status_10 = files.internacionales_psc_status_10_folder
        # if not os.path.exists(psc_status_10):
        #     os.makedirs(psc_status_10)
        #
        # # ---------------------------------- inicio creando archivo factura valida
        # with open(archivo_psc_base) as file, open(psc_status_10+output_psc_file_txt_name, "w") as output:
        #     # with open(invoice_txt) as file, open(output_txt_file, "w") as output:
        #     for index, line in enumerate(file):
        #         # output.write(line)
        #         if index == 1:
        #             line_1 = line.split("|")
        #             new_line_1 = self.replace_psc_num_po_and_status(line_1, num_po_txt_tmp, "10")
        #             output.write(new_line_1)
        #             output.write('\n')
        #             # fyl.write(str(paste()), '\n')
        #         else:
        #             output.write(line)
        #
        # output_path_psc_txt_file = f"{files.internacionales_tmp_psc_folder}{output_psc_file_txt_name}"
        # psc_number = output_psc_file_txt_name.replace('.txt', '')
        # print(f"PSC: {psc_number}")
        # print(f"PSC CREADO, STATUS ACTUALIZADO A: 10")
        # psc_file_txt = output_psc_file_txt_name
        # return psc_number, psc_file_txt
