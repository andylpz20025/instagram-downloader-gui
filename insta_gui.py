import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox, QFileDialog, QHBoxLayout, QProgressBar
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication
import instaloader

# DPI-Policy fix
QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

class InstaDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Instagram Downloader")
        self.setGeometry(100, 100, 500, 220)

        layout = QVBoxLayout()

        self.info_label = QLabel(
            "Instagram URL (Post/Album/Reel):\n"
            "(Alben, Reels, Fotos, Videos werden unterstützt)"
        )
        self.url_input = QLineEdit()

        self.login_btn = QPushButton("Login (optional)")
        self.login_btn.clicked.connect(self.login)

        self.download_btn = QPushButton("Download starten")
        self.download_btn.clicked.connect(self.download_content)

        self.progress = QProgressBar()
        self.progress.setVisible(False)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.login_btn)
        btn_layout.addWidget(self.download_btn)

        layout.addWidget(self.info_label)
        layout.addWidget(self.url_input)
        layout.addLayout(btn_layout)
        layout.addWidget(self.progress)

        self.setLayout(layout)

        self.loader = instaloader.Instaloader(
            save_metadata=False,
            download_comments=False
        )
        # User-Agent setzen, um Instagram zu täuschen
        self.loader.context._session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/114.0.0.0 Safari/537.36"
            )
        })
        self.logged_in = False

    def login(self):
        from PyQt6.QtWidgets import QInputDialog, QLineEdit

        username, ok1 = QInputDialog.getText(self, "Login", "Benutzername:")
        if not ok1 or not username:
            return
        password, ok2 = QInputDialog.getText(self, "Login", "Passwort:", QLineEdit.EchoMode.Password)
        if not ok2 or not password:
            return

        try:
            self.loader.login(username, password)
            self.logged_in = True
            QMessageBox.information(self, "Login", "Login erfolgreich!")
        except Exception as e:
            QMessageBox.critical(self, "Login Fehler", f"Login fehlgeschlagen:\n{str(e)}")

    def download_content(self):
        url = self.url_input.text().strip()
        if not url:
            QMessageBox.warning(self, "Fehler", "Bitte gib eine gültige Instagram-URL ein.")
            return

        # Nur Posts, Reels, Alben URLs - erkenne anhand /p/, /reel/, /tv/
        if not any(x in url for x in ["/p/", "/reel/", "/tv/"]):
            QMessageBox.warning(self, "Fehler", "Bitte gib eine gültige Instagram-Post-/Reel-URL ein (enthält /p/, /reel/ oder /tv/).")
            return

        folder = QFileDialog.getExistingDirectory(self, "Speicherort wählen")
        if not folder:
            return

        try:
            self.progress.setVisible(True)
            self.progress.setRange(0, 0)  # Busy indicator

            shortcode = url.rstrip('/').split('/')[-1]

            post = instaloader.Post.from_shortcode(self.loader.context, shortcode)

            self.loader.dirname_pattern = folder

            self.loader.download_post(post, target=post.owner_username)

            self.progress.setVisible(False)
            QMessageBox.information(
                self,
                "Erfolg",
                f"Download abgeschlossen!\nGespeichert in:\n{folder}/{post.owner_username}"
            )
        except Exception as e:
            self.progress.setVisible(False)
            QMessageBox.critical(self, "Fehler", f"Download fehlgeschlagen:\n{str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InstaDownloader()
    window.show()
    sys.exit(app.exec())
