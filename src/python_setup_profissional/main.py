"""Ponto de entrada da aplicação."""


def saudacao(nome: str = "mundo") -> str:
    """Retorna uma saudação para o nome informado."""
    return f"Olá, {nome}!"


def main() -> None:
    print(saudacao())


if __name__ == "__main__":
    main()
