import winreg
import os
import sys

def instalar_botao_direito():
    try:
        caminho_script = os.path.abspath("smart_folder.py")
        caminho_python = sys.executable 

        comando = f'"{caminho_python}" "{caminho_script}" "%1"'
        chave_path = r"SystemFileAssociations\.txt\shell\SmartFoldersAI"

        winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, chave_path)
        chave = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, chave_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(chave, "", 0, winreg.REG_SZ, "🪄 Resumir com SmartFolder AI")

        chave_comando_path = rf"{chave_path}\command"
        winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, chave_comando_path)
        chave_comando = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, chave_comando_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(chave_comando, "", 0, winreg.REG_SZ, comando)

        winreg.CloseKey(chave)
        winreg.CloseKey(chave_comando)
        print("Integração com Windows Registry concluída com sucesso.")

    except PermissionError:
        print("Erro: Execute o terminal como Administrador.")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    instalar_botao_direito()