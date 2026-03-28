import sys
import os
from google import genai

GOOGLE_API_KEY = "SUA CHAVE API AQUI"
client = genai.Client(api_key=GOOGLE_API_KEY)

def processar_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        prompt = f"Faça um resumo direto e claro do seguinte texto:\n\n{conteudo}"
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )

        diretorio_atual = os.path.dirname(caminho_arquivo)
        nome_arquivo = os.path.basename(caminho_arquivo)
        nova_pasta = os.path.join(diretorio_atual, "Resultados IA")

        if not os.path.exists(nova_pasta):
            os.makedirs(nova_pasta)

        novo_caminho_arquivo = os.path.join(nova_pasta, f"Resumo_{nome_arquivo}")
        with open(novo_caminho_arquivo, 'w', encoding='utf-8') as f:
            f.write(response.text)

    except Exception as e:
        print(f"Erro na execução: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        processar_arquivo(sys.argv[1])
