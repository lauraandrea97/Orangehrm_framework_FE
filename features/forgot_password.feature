Feature: Forgot password
  Como administrator
  Quiero resetear mi password en OrangeHRM
  Para acceder al sistema

@forgot
Scenario Outline: Validación de resetear la contraseña
    Given el usuario está en la página de login
    When hace click en forgot your password
    And ingresa el username "<user>"
    And hace click en Reset Password
    Then debería ver el mensaje "<resultado>"

    Examples:
      | user  | resultado                            |
      | test_g1 | Reset Password link sent successfully |


@forgot
Scenario Outline: Validación de resetear la contraseña con campos vacíos
    Given el usuario está en la página de login
    When hace click en forgot your password
    And ingresa el username "<user>"
    And hace click en Reset Password
    Then debería ver el mensaje "<resultado>"

    Examples:
      | user  | resultado    |
      | EMPTY | mensajeerror |
