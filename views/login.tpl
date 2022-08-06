%rebase("base.tpl")

	<h1 class="text-center">For easier surfing and for further acces you may log in.</h1>
	<h3 class="text-center" style="color:rgb(255, 38, 0);">{{!alert}}</h3>
	<center>
		<div class="back">
			<div class="div-center">
				<div class="content">
					<form action="/login/" method="post">

						<div class="form-group">
							<label for="emso">EMŠO :</label> <input class="form-control-lg" id="emso" name="emso" placeholder="Vpiši EMŠO" required="" type="number">
						</div>
						<br>

						<div class="form-group">
							<label for="ime">Username :</label> <input class="form-control-lg" id="ime" name="ime" placeholder="Vpiši ime" required="" type="text">
						</div>
						<br>

						<div class="form-group">
							<label for="rojstvo">Birthdate :</label> <input class="form-control-lg" id="rojstvo" name="rojstvo" placeholder="Vpiši rojstvo" type="date">
						</div>
						<br>

						<div class="form-group">
							<label for="email">Email :</label> <input class="form-control-lg" id="email" name="email" placeholder="Vpiši elektronski naslov" type="email">
						</div>
						<br>
						
						<div class="form-group">
							<label for="password">Password :</label> <input class="form-control-lg" id="password" name="password" placeholder="Enter Password" required="" type="password">
						</div>
						
						<input class="form-check-input" id="first_login" name="first_login" type="checkbox"> I don't have an account/register me!<br>
						<br>
						<div class="align-center">
							<button class="btn btn-success" type="submit">Log in</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	</center>
