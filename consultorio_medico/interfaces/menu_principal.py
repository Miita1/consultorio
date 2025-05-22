import customtkinter as ctk
from interfaces.editar_citas_usuario import EditarCitasUsuario
from interfaces.modulo_atencion_medica import ModuloAtencionMedica
from interfaces.receta_medica import RecetaMedica


class MenuPrincipal(ctk.CTkFrame):
    def __init__(self, master, controller, usuario):
        super().__init__(master)
        self.controller = controller
        self.master = master
        self.usuario = usuario

        self.label = ctk.CTkLabel(self, text="Menú Principal", font=("Arial", 24))
        self.label.pack(pady=30)

        # Botones del menú
        self.btn_registro = ctk.CTkButton(self, text="Registro de Pacientes", width=250, command=self.abrir_registro)
        self.btn_registro.pack(pady=10)

        self.btn_citas = ctk.CTkButton(self, text="Agendar Cita", width=250, command=self.abrir_gestion_citas)
        self.btn_citas.pack(pady=10)

        self.btn_editar_citas = ctk.CTkButton(self, text="Editar mis citas", command=self.abrir_editar_citas)
        self.btn_editar_citas.pack(pady=10)

        self.btn_atencion = ctk.CTkButton(self, text="Módulo de Atención Médica", width=250, command=self.abrir_atencion_medica)
        self.btn_atencion.pack(pady=10)

        self.boton_receta = ctk.CTkButton(self, text="Receta médica", command=self.abrir_receta_medica)
        self.boton_receta.pack(pady=10)

        self.btn_salir = ctk.CTkButton(self, text="Cerrar Sesión", command=self.volver_login, width=250)
        self.btn_salir.pack(pady=30)

        


    def abrir_registro(self):
        from interfaces.registro_paciente import RegistroPaciente
        self.destroy()
        registro = RegistroPaciente(self.master, self.controller, self.usuario)
        registro.pack(fill="both", expand=True)

    def abrir_gestion_citas(self):
        from interfaces.gestion_citas import AgendarCita
        self.destroy()
        cita = AgendarCita(self.master, self.controller, self.usuario)
        cita.pack(fill="both", expand=True)

    def abrir_editar_citas(self):
        self.destroy()
        vista = EditarCitasUsuario(self.master, self.controller, self.usuario)
        vista.pack(fill="both", expand=True)

    def abrir_atencion_medica(self):
        self.destroy()
        vista = ModuloAtencionMedica(self.master, self.controller, self.usuario)
        vista.pack(fill="both", expand=True)

    def abrir_receta_medica(self):
        self.destroy()
        vista = RecetaMedica(self.master, self.controller, self.usuario)
        vista.pack(fill="both", expand=True)


    def volver_login(self):
        from interfaces.login import LoginScreen
        self.destroy()
        login = LoginScreen(self.master, self.controller)
        login.pack(fill="both", expand=True)
