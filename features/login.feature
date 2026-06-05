Feature: Login OrangeHRM
  Como administrador
  Quiero iniciar sesión en OrangeHRM
  Para acceder al sistema

Background:
    Given el usuario está en la página de login

@login
Scenario Outline: Validación de Login exitoso con credenciales válidas
  When ingresa credenciales "<user>" y "<password>"
  Then debería ver "<resultado>"

  Examples:
    | user  | password | resultado |
    | Admin | admin123 | dashboard |


@login
Scenario Outline: Validación Login fallido con contraseña incorrecta
  When ingresa credenciales "<user>" y "<password>"
  Then debería ver "<resultado>"

  Examples:
    | user  | password | resultado    |
    | Admin | wrong    | mensajeerror |
    | wrong | admin123 | mensajeerror |


@login
Scenario Outline: Validación Login fallido con campos vacíos
  When ingresa credenciales "<user>" y "<password>"
  Then debería ver "<resultado>"

  Examples:
    | user  | password | resultado    |
    | EMPTY | EMPTY    | mensajeerror |
