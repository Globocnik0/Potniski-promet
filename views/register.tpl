%rebase("base.tpl")

	<h1 class="text-center">For easier surfing and for further acces you may log in.</h1>
	<h3 class="text-center" style="color:rgb(255, 38, 0);">{{!alert}}</h3>
	<center>
		<div class="back">
			<div class="div-center">
				<div class="content">
					<form action="/register/" method="post">

						<div class="form-group">
							<label for="emso">EMŠO :</label> <input class="form-control-lg" id="emso" name="emso" placeholder="Enter your EMŠO" required="" type="number">
						</div>
						<br>

						<div class="form-group">
							<label for="ime">Username :</label> <input class="form-control-lg" id="ime" name="ime" placeholder="Enter username" required="" type="text">
						</div>
						<br>

						<div class="form-group">
							<label for="rojstvo">Birthdate :</label> <input class="form-control-lg" id="rojstvo" name="rojstvo" placeholder="Enter birthdate" type="date">
						</div>
						<br>

						<div class="form-group">
							<label for="naslov">Addres :</label> <input class="form-control-lg" id="naslov" name="naslov" placeholder="Enter adress" type="text">
						</div>
						<br>

						<div class="form-group">
							<label for="email">Email :</label> <input class="form-control-lg" id="email" name="email" placeholder="Enter email" type="email">
						</div>
						<br>
						
						<div class="form-group">
							<label for="password">Password :</label> <input class="form-control-lg" id="password" name="password" placeholder="Enter Password" required="" type="password">
						</div>
						<br>
						
						<div class="align-center">
							<button class="btn btn-success" type="submit">Register</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	</center>