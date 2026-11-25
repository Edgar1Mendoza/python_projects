"""
Create a code that generates a loop that counts
elephants swinging in a spider web.
Loop should run 20 times.
"""

for i in range(1, 21):
    if i > 1:
        print(f"{i} elephants were swinging on a spider's web.")
        print('Seeing that the web held strong,', end=' ')
        print('they went to call anouther elephant.')

    else:
        print(f"{i} elephant was swinging on a spider's web.")
        print('Seeing that the web held strong,', end=' ')
        print('the elephant went to call anouther elephant.')
