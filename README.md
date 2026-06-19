# Projeto 06 - Pre-processamento de Imagens com OpenCV

Projeto do Lab 06 (ES510 - Introducao a IA, UFPE) com implementacoes de tecnicas classicas de processamento de imagens.

## Objetivo

Aplicar operacoes de visao computacional em etapas:

- leitura e conversao de espaco de cores;
- transformacoes geometricas;
- transformacoes em escala de cinza;
- processamento morfologico;
- filtragem e nitidez.

## Estrutura

```text
06/
├── README.md
├── requirements.txt
├── Docs/
│   └── [ES510]_Lab6.pdf
└── src/
    ├── a.py
    ├── b.py
    ├── c.py
    ├── d.py
    ├── e.py
    ├── validate.py
    └── data/
        ├── panda.jpg
        └── README.md
```

## Requisitos

- Python 3.10+
- numpy, matplotlib, opencv-python, ipython

## Setup

No PowerShell, a partir da pasta 06:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Dataset

O arquivo principal de entrada e src/data/panda.jpg.

Se necessario, siga orientacao em src/data/README.md para obter o pacote oficial.

## Execucao

Validacao automatica sem interface grafica:

```powershell
cd src
python validate.py
```

Execucao por secao:

```powershell
cd src
python a.py
python b.py
python c.py
python d.py
python e.py
```

## Resultado esperado

- validacoes com mensagens [OK] para cada secao;
- confirmacao final ALL VALIDATIONS PASSED;
- resultados numericos coerentes com o material do laboratorio.

## Observacoes

- os scripts usam estilo de laboratorio com #%%;
- para reproducao fiel, execute na ordem a -> e.

## Arquivos-chave

- src/validate.py — validação automatizada de todas as seções
- src/a.py — operações básicas e conversão de cores
- src/b.py — transformações geométricas
- src/c.py — transformações em escala de cinza
- src/d.py — processamento morfológico
- src/e.py — filtragem de imagens
- src/questoes.py — respostas das questões do Lab (Otsu vs manual)
