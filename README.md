# 📚 Estudo OOP Biblioteca

Projeto simples em Python utilizando Programação Orientada a Objetos (POO) para simular uma biblioteca. Os livros são armazenados em memória com suporte a adição, remoção, listagem e busca por título.

---

## 🚀 Funcionalidades

- Adicionar livros à biblioteca  
- Remover livros pelo ISBN  
- Listar todos os livros cadastrados  
- Buscar livros pelo título  

---

## 🗂️ Estrutura do Projeto

```
estudo_OOP_biblioteca/
│
├── biblioteca.py      # Classe Biblioteca
├── livro.py           # Classe Livro
├── main.py            # Script principal com testes
├── .gitignore         # Arquivos ignorados pelo Git
└── README.md          # Documentação do projeto
```

---

## ⚙️ Como Funciona

- `livro.py`: Define a classe `Livro`, com título, autor, ano e ISBN. Possui um método `__str__` para exibição formatada.
- `biblioteca.py`: Define a classe `Biblioteca`, que mantém uma lista de livros e permite adicionar, remover, listar e buscar livros.
- `main.py`: Cria objetos `Livro`, adiciona na biblioteca, exibe a lista, busca por título e remove livro por ISBN.

---

## ▶️ Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/nathanlemos1/estudo_OOP_biblioteca.git
```

2. Acesse o diretório:
```bash
cd estudo_OOP_biblioteca
```

3. Execute o script:
```bash
python main.py
```

---

## 🧠 Tecnologias Utilizadas

- Python 3
- Programação Orientada a Objetos (POO)

---

## 📄 .gitignore

```
.venv/
__pycache__/
```

---

## ✍️ Autor

**Nathan Lemos**
