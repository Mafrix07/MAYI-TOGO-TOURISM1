import 'package:flutter/material.dart';
import 'package:frontend_new/page/login_page.dart';

class SignInPage extends StatelessWidget {
  const SignInPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: kBackgroundColor,
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.symmetric(horizontal: 30),
          child: Column(
            children: [
              const SizedBox(height: 60),
              Image.asset('assets/image/mon_image_logo.png', height: 100),
              const SizedBox(height: 40),
              const Text(
                'Bon retour parmi nous',
                style: TextStyle(color: kTextColor, fontSize: 24, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 40),
              _buildSimpleInput(Icons.email_outlined, 'E-mail'),
              const SizedBox(height: 15),
              _buildSimpleInput(Icons.lock_outline, 'Mot de passe', isPassword: true),
              const SizedBox(height: 30),

              SizedBox(
                width: double.infinity,
                height: 55,
                child: ElevatedButton(
                  onPressed: () {

                },
                  style: ElevatedButton.styleFrom(
                    backgroundColor: kPrimaryColor,
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(30)),
                  ),
                  child: const Text('Se connecter', style: TextStyle(color: Colors.white, fontSize: 18)),
                ),

              ),
              const SizedBox(height: 20),
              TextButton(
                onPressed: (){
                  Navigator.pop(context);
                },
                child: const Text("Pas encore de compte? S'inscrire", style: TextStyle(color: kTextColor)),
              ),

            ],
          ),
        ),
      ),
    );
  }
  Widget _buildSimpleInput(IconData icon, String hint, {bool isPassword = false}) {
    return Container(
      decoration: BoxDecoration(color: kInputFieldColor, borderRadius: BorderRadius.circular(15)),
      child: TextField(
        obscureText: isPassword,
        decoration: InputDecoration(
          hintText: hint,
          prefixIcon: Icon(icon, color: Colors.grey),
          border: InputBorder.none,
          contentPadding: const EdgeInsets.symmetric(vertical: 18),
        ),
      ),
    );
  }
}

