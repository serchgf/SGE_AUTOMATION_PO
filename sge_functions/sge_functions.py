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


class Pasos_prueba:

    def __init__(self, step_index: str, action: str, step_input: str, expected_result: str):
        #self.__Index = Index
        self.__step_index = step_index
        self.__action = action
        self.__step_input = step_input
        self.__expected_result = expected_result

    def obtener_step_index(self):
        return self.__step_index

    def obtener_action(self):
        return self.__action

    def obtener_step_input(self):
        return self.__step_input

    def obtener_expected_result(self):
        return self.__expected_result

    def actualizar_step_index(self, step_index: str):
        self.__step_index = step_index

    def actualizar_action(self, action: str):
        self.__action = action

    def actualizar_step_input(self, step_input: str):
        self.__step_input  = step_input

    def actualizar_expected_result(self, expected_result: str):
        self.__expected_result = expected_result

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f"step_index={self.__step_index}, action={self.__action}, step_input={self.__step_input}, expected_result={self.__expected_result}"


class sge_functions:

    img_pantalla_inicial = images.img_pantalla_inicial
    img_error_connection = images.img_error_connection
    img_inicio_orden_de_compra = images.img_inicio_orden_de_compra
    img_consulta_orden_de_compra = images.img_consulta_orden_de_compra
    img_confirmacion_colocada = images.img_confirmacion_colocada
    img_header_orden_de_compra = images.img_header_orden_de_compra
    img_confirmada_por_proveedor = images.img_status_confirmada_por_proveedor
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

    #inv_base_text_file = files.inv_base_txt_file
    factura_valida_text_file = txt_files_path.fact_valida_txt_file
    factura_invalida_text_file = txt_files_path.fact_invalida_txt_file


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

    def crear_objeto(self, line: list):
        # Line[0] = index. Line[1] = Action. Line[2] = input. Line[3] = expected_result
        my_step = Pasos_prueba(line[0], line[1], line[2], line[3])
        return my_step

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

    def crear_lista_objetos(self, csv_file):
        lista_objetos = []
        # Line[0] = index. Line[1] = Action. Line[2] = input.
        with open(csv_file, newline='') as file:
            file_reader = csv.reader(file)
            next(file_reader)
            for line in file_reader:
                my_step = self.crear_objeto(line)
                my_step.actualizar_step_input(self.clean_input_text(my_step.obtener_step_input()))
                lista_objetos.append(my_step)
        return lista_objetos

    def clean_input_text(self, step_input):
        if '"' in step_input:
            cleaned_input = step_input.replace('"', "")
            # print(cleaned_input)
            return str(cleaned_input)
        # print(step_input)
        return step_input

    def type_cmds(self, cmd):
        try:
            pa.typewrite(cmd)
            time.sleep(1)
        except TypeError:
            self.type_cmds(cmd)


    def read_general_commands(self, object_list, img_r_Click, img_doubleClick, archivo_productos):

        for obj in object_list:
            print(obj.obtener_action())
            self.press_general_commands(obj.obtener_step_input(), img_r_Click, img_doubleClick, archivo_productos)
        # for cmd in command_list:
        #     self.press_general_commands(cmd, img_r_Click, img_doubleClick)

    def press_Test_hotkey(self, cmd):
        if "ctrl" in cmd:
            hotkey = cmd.split('+')
            pa.hotkey(hotkey[0], hotkey[1])

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
            #pa.press('tab')
            pa.hotkey(commons_cmds.tab)

        elif cmd == commons_cmds.space:
            pa.press('space')

        elif cmd == "leer_archivo" or cmd == "read_file":
            #pa.press('tab')
            #with open(txt_files_path.txt_file, 'r') as f1:
            with open(archivo_productos, 'r') as f1:
                for line in f1:
                    print(line)
                    pa.typewrite(line)
                #pa.press('tab')

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
            self.subir_factura_invalida_sftp()

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
            sftp_connection.sftp_connection(data_sftp_connection.sftp_hostname, data_sftp_connection.sftp_username, data_sftp_connection.sftp_hostname)
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

    def press_hotkeys(self, cmd):
        pa.hotkey(str(cmd))

    def take_screenshot(self, message):
        print("taking screenshot " + message )
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
                #self.create_inv_txt_file()
                self.close_as = 0
                return True
        except:
            print("An error has occurred, PO no created")
            message = "Test_failed"
            time.sleep(1)
            self.take_screenshot(message)
            assert False, "An error has occurred, PO no created"


    def create_general_po(self, object_list_to_process, img_r_Click: None, img_doubleClick: None, archivo_productos: None, fact_valida:None, fact_invalida: None):
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
        # obtain name of directory descomentar
        #self.create_report_directory()
        #shutil.move(f"screenshots/funcionaScreenshot.png", f"{path_to_move}/{img_to_move}")
        try:
            shutil.move(f"screenshots/my_screenshot.png", f"{path_to_move}/{img_to_move}")
            file_source = files.directory_tmp_file
            file_destination = path_to_move
            copy_file_destination = files.valid_inv_confirmed_po_file
            get_files = os.listdir(file_source)
            for f in get_files:
                try:
                    shutil.copy(file_source + f, copy_file_destination + f)
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
            #print(headerOrdencompra)
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
            #with open(invoice_txt) as file, open(output_txt_file, "w") as output:
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
            #with open(invoice_txt) as file, open(output_txt_file, "w") as output:
                for index, line in enumerate(file):
                    # output.write(line)
                    if index == 1:
                        line_1 = line.split("|")
                        new_line_1 = self.replace_list_index_1(line_1, nombre_po)
                        output.write(new_line_1)
                        # fyl.write(str(paste()), '\n')
                    else:
                        output.write(line)
            #---------------------------------- fin creando archivo factura INVALIDA
        else:
            print("header no encontrado")
            print(headerOrdencompra)
        #return output_txt_file

    def replace_list_index_1(self, lista_a, nombre_po):

        nspacesl_0 = 25 - len(nombre_po)
        nspacesl_1 = 25 - len("INV" + nombre_po)

        lista_a[0] = nombre_po + " " * nspacesl_0
        lista_a[1] = "INV" + nombre_po + " " * nspacesl_1
        #campo Fecha
        lista_a[3] = datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")

        # print("modificado")
        nl = []
        for i in lista_a:
            if i != lista_a[-1]:
                i = i + "|"
            nl.append(i)
        return "".join(map(str, nl))

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

    def validar_status_post_job(self, img_status):
        time.sleep(1)
        try:
            coord_xy = pa.locateOnScreen(img_status)
            #print("6666666666666666666666666666666666666666666666666")
            #print(coord_xy)
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
        time.sleep(2)
        print("Validating PO Status...")
        in_screen = pa.locateOnScreen(img_status_po)
        if in_screen != '' or in_screen is not None:
            print(in_screen)
            print(f"PO Status {nombre_status} Correct...")
            # print(f"copiando factura con status: {nombre_status} a /facturas_generadas/... ")
            #
            # mover factura confirmada valid a facturas_generadas_procesados
            shutil.move(f"{files.valid_inv_confirmed_po_file}INV-{self.po_seleccionada}.txt",
                        f"{files.processed_inv_file}INV-{self.po_seleccionada}.txt")

            #mover factura invalida mover a procesados con renombre invalida
            shutil.move(f"{files.invalid_inv_folder}INV-{self.po_seleccionada}.txt",
                        f"{files.processed_inv_file}INV-{self.po_seleccionada}INVALIDA.txt")
            return True
        else:
            print("PO status not expected...")
            message = ("PO status not expected...")
            self.take_screenshot(message)
            # mover factura valida mover a procesados
            shutil.move(f"{files.valid_inv_confirmed_po_file}INV-{self.po_seleccionada}.txt",
                        f"{files.processed_inv_file}INV-{self.po_seleccionada}.txt")
            #mover factura invalida mover a procesados con renombre invalida
            shutil.move(f"{files.invalid_inv_folder}INV-{self.po_seleccionada}.txt",
                        f"{files.processed_inv_file}INV-{self.po_seleccionada}INVALIDA.txt")
            return False

    def mover_factura_status_en_trasito(self):
        # mover factura confirmada valid a facturas_generadas_en transito
        try:
            shutil.move(f"{files.processed_inv_file}INV-{self.po_seleccionada}.txt",
                        f"{files.inv_en_transito_folder}INV-{self.po_seleccionada}.txt")
        except:
            print("No se copio factura procesada a carpeta /facturas_generadas/en_transito/")

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
                #pa.typewrite(n_sucursal)
        except:
            print("EXCEPT Error, Sucursal no seleccionada...")


# ----------------------------------------------------------------------------SFTP
    def sftp_connection(self):
        sftp_con = sftp_connection()
        sftp_con.sftp_connection(data_sftp_connection.sftp_hostname, data_sftp_connection.sftp_username, data_sftp_connection.sftp_password)

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
        pa.typewrite(f"put {file_source+random_inv}")
        #pa.press('enter')
        self.po_seleccionada = str(random_inv).replace("INV-", "").replace(".txt", "")

    def subir_factura_invalida_sftp(self):
        """ cmd debe ser la ruta en el servidor donde se subira el archivo"""
        file_source = files.invalid_inv_folder
        get_files = os.listdir(file_source)
        random_inv = random.choice(get_files)
        print(f"INV seleccionada: {random_inv}")
        pa.typewrite(f"put {file_source+random_inv}")
        #pa.press('enter')
        self.po_seleccionada = str(random_inv).replace("INV-", "").replace(".txt", "")

    def validar_job_status_ok(self):
        time.sleep(2)
        print("Validating job Status...")
        in_sftp = pa.locateOnScreen(self.img_sftp_connection_valid)
        if in_sftp != '' or in_sftp is not None:
            #n_sftp != '' or in_sftp != None:
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
            #n_sftp != '' or in_sftp != None:
            print(in_sftp)
            return True
        else:
            print("Job status not expected...")
            return False


# functions to create the new inv text file

    def create_inv_international_valid_invalid_txt_file(self):
        headerOrdencompra = pa.locateCenterOnScreen(self.img_header_orden_de_compra)
        if headerOrdencompra != "":
            # print("-----------------------------")
            # print("encontrado")
            #print(headerOrdencompra)
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
            #with open(invoice_txt) as file, open(output_txt_file, "w") as output:
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
            #with open(invoice_txt) as file, open(output_txt_file, "w") as output:
                for index, line in enumerate(file):
                    # output.write(line)
                    if index == 1:
                        line_1 = line.split("|")
                        new_line_1 = self.replace_list_index_1(line_1, nombre_po)
                        output.write(new_line_1)
                        # fyl.write(str(paste()), '\n')
                    else:
                        output.write(line)
            #---------------------------------- fin creando archivo factura INVALIDA
        else:
            print("header no encontrado")
            print(headerOrdencompra)
        #return output_txt_file

# ----------------------------------------------------------------------------SFTP