# Lab 06 - Pre-processamento de Dados de Imagem

Projeto da disciplina ES510 (Introducao a IA - UFPE) para implementacao das tecnicas de pre-processamento apresentadas no material [ES510]_Lab6.pdf.

## Objetivo

Aplicar tecnicas de processamento de imagem com OpenCV em Python, cobrindo:

- operacoes basicas com imagens;
- conversao de espaco de cores;
- transformacoes geometricas;
- transformacoes em escala de cinza;
- processamento morfologico;
- filtragem de imagens.

## Estrutura

| Arquivo | Secao do Lab | Escopo |
|---|---|---|
| src/a.py | 1.4.1 e 1.4.2 | Operacoes basicas e conversao de cores |
| src/b.py | 1.4.3 | Transformacoes geometricas |
| src/c.py | 1.4.4 | Transformacoes em escala de cinza |
| src/d.py | 1.4.5 | Operacoes morfologicas |
| src/e.py | 1.4.6 | Filtros e nitidez |
| src/validate.py | Validacao | Checagem funcional das secoes |
| Docs/[ES510]_Lab6.pdf | Referencia | Material didatico oficial |

## Requisitos

- Python 3.7+
- Dependencias em requirements.txt

Instalacao:

```bash
pip install -r requirements.txt
```

## Dataset

O projeto usa a imagem panda.jpg na pasta src/data.

Download do pacote oficial:
https://certification-data.obs.cn-north-4.myhuaweicloud.com/ENG/HCIP-AI%20EI%20Developer/V2.5/chapter2/cv.zip

As instrucoes detalhadas estao em src/data/README.md.

## Execucao

Validacao automatica:

```bash
cd src
python validate.py
```

Execucao por secao (ambiente interativo com suporte a celulas):

```bash
cd src
python a.py
python b.py
python c.py
python d.py
python e.py
```

## Resultado Esperado

- Scripts executam sem erros com o dataset configurado.
- Saidas numericas principais seguem o PDF, incluindo:
	- tipo e dimensao da imagem;
	- limiar simples 127.0;
	- limiar Otsu 108.0.

## Observacoes

- Os arquivos seguem o estilo de laboratorio com blocos #%%.
- Alguns blocos usam comandos tipicos de notebook/ambiente interativo.
