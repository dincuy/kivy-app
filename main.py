from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class MyKivyApp(App):
    def build(self):
        # Layout utama
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Input teks
        self.text_input = TextInput(
            hint_text="Masukkan nama Anda",
            size_hint=(1, 0.2),
            multiline=False
        )
        layout.add_widget(self.text_input)

        # Label untuk menampilkan hasil
        self.label = Label(
            text="Halo, Selamat datang di aplikasi Kivy!",
            size_hint=(1, 0.6)
        )
        layout.add_widget(self.label)

        # Tombol
        button = Button(
            text="Sapa Saya",
            size_hint=(1, 0.2),
            background_color=(0.1, 0.6, 0.8, 1)
        )
        button.bind(on_press=self.on_button_press)
        layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        # Ambil teks dari input dan tampilkan di label
        name = self.text_input.text
        if name.strip():
            self.label.text = f"Halo, {name}! Senang bertemu dengan Anda!"
        else:
            self.label.text = "Halo, Masukkan nama Anda terlebih dahulu!"


if __name__ == "__main__":
    MyKivyApp().run()
