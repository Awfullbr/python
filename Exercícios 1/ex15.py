from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você degeja: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ângulo, tangente))
#CODIGOS PRECIOSOS : MATH.RADIANS, MATH.SIN, MATH.COS E MATH.TAN