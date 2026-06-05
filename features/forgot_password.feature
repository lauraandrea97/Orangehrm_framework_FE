Feature: Forgot password
  Como administrator
  Quiero resetear mi password en OrangeHRM
  Para acceder al sistema

@forgotpassword
Scenario: Validación de resetear la contraseña
  Given el usuario está en la página de login
  When hace click en forgot you password
  Then debería ver el modal de Reset Password