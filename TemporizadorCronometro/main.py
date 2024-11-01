from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

class CronometroTemporizador(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Definindo como o cronometro iniciará
        self.cronometro_ativo = False
        self.cronometro_segundos = 0
        
        # Definindo como o temporizador iniciará
        self.temporizador_ativo = False
        self.temporizador_segundos = 0
        
        # Oque será escrito dentro da box cronometro
        self.label_cronometro = Label(text="Cronômetro: 00:00", font_size=32) #dentro da box cronometro, escrevi oque eu quero que apareça e defini um tamanho
        self.add_widget(self.label_cronometro)
        
        # criando os botoes do cronometro
        self.botoes_cronometro = BoxLayout(size_hint_y=None, height=50)
        
        botao_iniciar = Button(text="Iniciar Cronômetro") #Criei um botao e nele dei o nome INICIAR CRONOMETRO
        botao_iniciar.bind(on_press=self.iniciar_cronometro) #Ao ser precionado ele exetuca a funcao inicar_cronometro
        
        botao_pausar = Button(text="Pausar Cronômetro") #Criei um botao e nele dei o nome PAUSAR CRONOMETRO
        botao_pausar.bind(on_press=self.pausar_cronometro)#Ao ser precionado ele exetuca a funcao pausar_cronometro
        
        botao_zerar = Button(text="Zerar Cronômetro") #Criei um botao e nele dei o nome ZERAR CRONOMETRO
        botao_zerar.bind(on_press=self.zerar_cronometro)  #Ao ser precionado ele exetuca a funcao zerar_cronometro
        
        
        self.botoes_cronometro.add_widget(botao_iniciar) 
        self.botoes_cronometro.add_widget(botao_pausar)
        self.botoes_cronometro.add_widget(botao_zerar)
        self.add_widget(self.botoes_cronometro)


        
        # Definindo como o temporizador iniciará
        self.label_temporizador = Label(text="Temporizador: 00:00", font_size=32) #dentro da box cronometro, escrevi oque eu quero que apareça e defini um tamanho
        self.add_widget(self.label_temporizador)  #*****

        
        
        # Criando uma caixa para poder iniserir um tempo para o temporizador 
        self.entrada_tempo = TextInput(hint_text="Tempo em segundos", multiline=False, size_hint_y=None, height=50)
        self.add_widget(self.entrada_tempo)
        
        # Criei um botão para iniciar o temporizador
        self.botao_iniciar_temporizador = Button(text="Iniciar Temporizador", size_hint_y=None, height=50)
        self.botao_iniciar_temporizador.bind(on_press=self.iniciar_temporizador) #Ao ser precionado ele exetuca a funcao zerar_cronometro
        self.add_widget(self.botao_iniciar_temporizador)
        
        # utilizando classe clock e o parametro schedule_interval implica que a cada segundo, o Kivy chama o método atualizar_tempo, o que permite incrementar o cronômetro e decrementar o temporizador, atualizando-os na interface.
        Clock.schedule_interval(self.atualizar_tempo, 1)
    
    def iniciar_cronometro(self, instance): #ao precionar botao Iniciar Cronometro, ele inica a contagagem
        self.cronometro_ativo = True #inicar a contagem
    
    def pausar_cronometro(self, instance):  #ao precionar botao pausar Cronometro, ele pausa a contagem
        self.cronometro_ativo = False #pausa a contagem
    
    def zerar_cronometro(self, instance):  #ao precionar botao Zerar Cronometro, ele zera a contagagem
        self.cronometro_ativo = False #para o cronometro
        self.cronometro_segundos = 0 #define com cronometro com 0 segundos
        self.label_cronometro.text = "Cronômetro: 00:00" 
    
    def iniciar_temporizador(self, instance): #Inicia quando o botao inicar temporziador é iniciado.
        try:
            self.temporizador_segundos = int(self.entrada_tempo.text)  #coverte oque foi escrito na caixa de entrada em um numero inteiro e o armazena
            self.temporizador_ativo = True #inica o temporizador
        except ValueError:
            self.label_temporizador.text = "Por favor, insira um número válido!" #caso insira alguma coisa que nao seja numero, exibe a mensagem de erro
    
    def atualizar_tempo(self, dt): #Essa funcao ocorre automaticamente, devido ao  Clock schedule interval
        #atualizacao do cronometro
        if self.cronometro_ativo:
            self.cronometro_segundos += 1
            minutos = self.cronometro_segundos // 60 #converte o segundos, para minutos
            segundos = self.cronometro_segundos % 60 # o restao da divisao resulta no segundos restantes
            self.label_cronometro.text = f"Cronômetro: {minutos:02}:{segundos:02}"
        
        # Atualização do temporizador
        if self.temporizador_ativo:
            if self.temporizador_segundos > 0:
                self.temporizador_segundos -= 1
                minutos = self.temporizador_segundos // 60 #converte o segundos, para minutos
                segundos = self.temporizador_segundos % 60 # o restao da divisao resulta no segundos restantes
                self.label_temporizador.text = f"Temporizador: {minutos:02}:{segundos:02}" #atualiza a box temporizador
            else:
                self.label_temporizador.text = "Temporizador finalizado!" #Quando o temporizador for igual a 0, exibe a mensagem de finalizacao
                self.temporizador_ativo = False 

class CronometroApp(App):
    def build(self):
        return CronometroTemporizador()

if __name__ == "__main__":
    CronometroApp().run()