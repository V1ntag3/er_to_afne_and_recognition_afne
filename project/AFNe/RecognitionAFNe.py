def closure( states, delta):
        S = set(states)
        notVisited = list(states)
        while len(notVisited) > 0:
            q = notVisited.pop()
            if (q, '') in delta:
                new = delta[(q, '')].difference(S)
                S.update(new)
                notVisited.extend(new)
        return S
class RecognitionAFNe():

    def __init__(self):
        self.message = "Recognizer AFNe"

    # Essa função avalia se uma cadeia é aceita ou não por um Autômato Finito Determinístico de Estado Vazios (AFDe)
    def VerificationAFe( Q, sigma, delta, q0, F, chainOfCharacters):
        activeStates = closure({q0}, delta)
        for symbol in chainOfCharacters:
            new = set()
            for q in activeStates:
                if (q, symbol) in delta:
                    new.update(closure( delta[(q, symbol)], delta))
            activeStates = new
        return len(activeStates.intersection(F)) != 0
    # Função cria uma lista de estados que nao foram visitados para que estados repetidos nao sejam considerados,
    # dai verifica se e existe uma transicao vazia e ela leva a um estado que nao estava no fechamento e assim o estado passa a estar no fechamento
