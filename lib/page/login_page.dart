import 'package:flutter/material.dart';
import'package:frontend_new/page/Sign_in_page.dart';
//Définition des couleurs
const Color kPrimaryColor = Color(0xFF6A9FB5);
const Color kInputFieldColor = Color(0xFFE8F1F5);
const Color kBackgroundColor = Color(0xFFFBFDFF);
const Color kTextColor = Color(0xFF2F4F4F);


class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      backgroundColor: kBackgroundColor,
      body: SafeArea(
          child: SingleChildScrollView(
            padding: const EdgeInsets.symmetric(horizontal:30.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                SizedBox(height: 50),

                // Insertion du logo
                Image.asset(
                  'assets/image/mon_image_logo.png',
                  height: 80,
                  fit: BoxFit.contain,
                ),

                const SizedBox(height: 30),

                // Ajout des titres

                const Text(
                  'Votre voyage commence ici',
                  textAlign: TextAlign.center,
                  style: TextStyle(
                    color: kTextColor,
                    fontSize: 22,
                    fontWeight: FontWeight.bold,
                    fontFamily: 'Georgia' // La police
                  ),
                ),
                const SizedBox(height: 10),
                const Text(
                  'Faites le premier pas',
                  textAlign: TextAlign.center,
                  style: TextStyle(
                    color: kTextColor,
                    fontSize: 16,
                    fontWeight: FontWeight.w400,
                  ),
                ),

                const SizedBox(height: 40),

                // Les champs de saisie

                _buildInputField(Icons.email_outlined, 'E-mail'),
                const SizedBox(height: 15),
                _buildInputField(Icons.person_outline, 'Nom d\' utilisateur'),
                const SizedBox(height: 15),
                _buildInputField(Icons.lock_outline, 'Mot de passe', isPassword: true),
                const SizedBox(height: 15),
                _buildInputField(Icons.lock_clock_outlined, 'Confirmer le mot de passe', isPassword: true),

                const SizedBox(height: 30),

                // Le bouton d'inscription

                SizedBox(
                  width: double.infinity,
                  height: 55,
                  child: ElevatedButton(
                    onPressed: () {

                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: kPrimaryColor,
                      foregroundColor: Colors.white,
                      elevation: 0,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(30),
                      )
                    ),
                    child: const Text(
                      'S\'inscrire',
                      style: TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ),

                const SizedBox(height: 25),

                // le séparateur "or"

                const Row(
                  children: [
                    Expanded(child: Divider(color: Colors.grey,thickness: 0.5)),
                    Padding(
                      padding: EdgeInsets.symmetric(horizontal: 10),
                      child: Text('ou', style: TextStyle(color: Colors.grey)),
                    ),
                    Expanded(child: Divider(color: Colors.grey, thickness: 0.5)),
                  ],
                ),

                const SizedBox(height: 25),

                // les boutons sociaux(facebook, apple, google)

                const Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    _SocialIcon(icon: Icons.facebook),
                    SizedBox(width: 30),
                    _SocialIcon(icon: Icons.apple),
                    SizedBox(width: 30),
                    _SocialIcon(icon: Icons.g_mobiledata_rounded),
                  ],
                ),

                const SizedBox(height: 35),

                // Le lien "déjà un compte?"

                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    const Text(
                      'Déjà un compte ?',
                      style: TextStyle(color: kTextColor, fontSize: 15),
                    ),
                    GestureDetector(
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (context) => const SignInPage()),
                        );
                      },
                      child: const Text(
                        'Se connecter',
                        style: TextStyle(
                          color: kTextColor,
                          fontWeight: FontWeight.bold,
                          decoration: TextDecoration.underline,
                        ),
                      ),
                    ),
                  ],
                ),

                const SizedBox(height: 20),


              ],

            ),
          )

      ),
    );

  }
  // Cette fonction crée le design de tes champs de texte (Email, Username, etc.)
  Widget _buildInputField(IconData icon, String hintText, {bool isPassword = false}) {
    return Container(
      decoration: BoxDecoration(
        color: kInputFieldColor, // Utilise la couleur claire définie en haut
        borderRadius: BorderRadius.circular(15), // Arrondi les coins
      ),
      child: TextField(
        obscureText: isPassword,
        decoration: InputDecoration(
          hintText: hintText,
          prefixIcon: Icon(icon, color: Colors.grey),
          border: InputBorder.none, // Enlève la ligne noire par défaut
          contentPadding: const EdgeInsets.symmetric(vertical: 18),
        ),
      ),
    );
  }
}
// Widget d'aide pour les icônes sociales (simples cercles vides ici)
class _SocialIcon extends StatelessWidget {
  final IconData icon;
  const _SocialIcon({required this.icon});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        shape: BoxShape.circle,
        border: Border.all(color: Colors.grey.shade400, width: 1),
      ),
      child: Icon(icon, color: Colors.black87, size: 28),
    );
  }
}
