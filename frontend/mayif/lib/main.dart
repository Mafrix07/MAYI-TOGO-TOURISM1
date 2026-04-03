import 'package:flutter/material.dart';
import 'views/splash_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Mayi - Togo Tourism',
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF1A237E), // Bleu profond 
          primary: const Color(0xFF1A237E),
          secondary: const Color(0xFFFFC107), // Ambre/Or     
          surface: const Color(0xFFF8F9FA),
        ),
        textTheme: const TextTheme(
          headlineLarge: TextStyle(fontWeight: FontWeight.bold, color: Color(0xFF1A237E)),
          titleLarge: TextStyle(fontWeight: FontWeight.w600, fontSize: 18),
        ),
        cardTheme: CardThemeData(
          elevation: 4,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
        ),
      ),
      home: const SplashScreen(),
    );
  }
}


class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int _selectedIndex = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Theme.of(context).colorScheme.surface, 
      body: SafeArea(
        child: SingleChildScrollView(
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,   
              children: [
                const SizedBox(height: 30),
                // Header section
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text("Bienvenue au Togo,", style: TextStyle(color: Colors.grey[600], fontSize: 16)),
                        const Text("Explorez le Togo !", style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold, color: Color(0xFF1A237E))),
                      ],
                    ),
                    const CircleAvatar(
                      radius: 25,
                      backgroundImage: NetworkImage('https://i.pravatar.cc/150?u=a042581f4e29026704d'),
                    )
                  ],
                ),
                const SizedBox(height: 30),
                // Search Bar
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 20),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(15),  
                    boxShadow: [BoxShadow(color: Colors.black.withAlpha(12), blurRadius: 10, offset: const Offset(0, 5))],  
                  ),
                  child: const TextField(
                    decoration: InputDecoration(
                      hintText: "Où voulez-vous aller ?",     
                      border: InputBorder.none,
                      icon: Icon(Icons.search, color: Color(0xFF1A237E)),
                    ),
                  ),
                ),
                const SizedBox(height: 30),
                // Categories
                const Text("Catégories", style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
                const SizedBox(height: 15),
                SingleChildScrollView(
                  scrollDirection: Axis.horizontal,
                  child: Row(
                    children: [
                      _buildCategoryItem(Icons.hotel, "Hôtels", true),
                      _buildCategoryItem(Icons.restaurant, "Restos", false),
                      _buildCategoryItem(Icons.map, "Guides", false),
                      _buildCategoryItem(Icons.car_rental, "Transport", false),
                    ],
                  ),
                ),
                const SizedBox(height: 30),
                // Top Services / Recommendations
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    const Text("Recommandations", style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
                    TextButton(onPressed: () {}, child: const Text("Voir tout", style: TextStyle(color: Color(0xFF1A237E)))),
                  ],
                ),
                const SizedBox(height: 10),
                // horizontal list of service cards
                SizedBox(
                  height: 300,
                  child: ListView(
                    scrollDirection: Axis.horizontal,
                    children: [
                      _buildServiceCard("Hôtel du 2 Février", "Lomé, Togo", "https://tse2.mm.bing.net/th/id/OIP.F8Q5w4Rj5-8lCF2iYTV2IwHaLH?rs=1&pid=ImgDetMain&o=7&rm=3", "75 000 FCFA"), 
                      _buildServiceCard("Cascade de Kpimé", "Kpalimé", "https://explorewithsandeep.com/wp-content/uploads/2023/09/IMG_20230708_140448-1024x576.jpg", "Gratuit"),
                      _buildServiceCard("Plage de Baguida", "Baguida", "https://quefairealome.com/wp-content/uploads/2023/10/WhatsApp-Image-2023-10-19-at-17.44.48-1024x613.jpeg", "1 000 FCFA"),
                    ],
                  ),
                ),
                const SizedBox(height: 30),
              ],
            ),
          ),
        ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _selectedIndex,
        onTap: (index) => setState(() => _selectedIndex = index),
        selectedItemColor: const Color(0xFF1A237E),
        unselectedItemColor: Colors.grey,
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home_rounded), label: 'Accueil'),
          BottomNavigationBarItem(icon: Icon(Icons.favorite_rounded), label: 'Favoris'),
          BottomNavigationBarItem(icon: Icon(Icons.confirmation_number_rounded), label: 'Résas'),
          BottomNavigationBarItem(icon: Icon(Icons.person_rounded), label: 'Profil'),
        ],
      ),
    );
  }

  Widget _buildCategoryItem(IconData icon, String label, bool isSelected) {
    return Padding(
      padding: const EdgeInsets.only(right: 15.0),
      child: Column(
        children: [
          Container(
            padding: const EdgeInsets.all(15),
            decoration: BoxDecoration(
              color: isSelected ? const Color(0xFF1A237E) : Colors.white,
              borderRadius: BorderRadius.circular(15),        
              boxShadow: isSelected ? null : [BoxShadow(color: Colors.black.withAlpha(12), blurRadius: 10)],
            ),
            child: Icon(icon, color: isSelected ? Colors.white : const Color(0xFF1A237E)),
          ),
          const SizedBox(height: 8),
          Text(label, style: TextStyle(fontWeight: isSelected ? FontWeight.bold : FontWeight.normal, fontSize: 13)),        
        ],
      ),
    );
  }

  Widget _buildServiceCard(String title, String location, String imageUrl, String price) {
    return Container(
      width: 220,
      margin: const EdgeInsets.only(right: 20),
      child: Card(
        clipBehavior: Clip.antiAlias,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,       
          children: [
            Stack(
              children: [
                Image.network(imageUrl, height: 160, width: double.infinity, fit: BoxFit.cover),
                Positioned(
                  top: 10,
                  right: 10,
                  child: Container(
                    padding: const EdgeInsets.all(5),
                    decoration: const BoxDecoration(color: Colors.white, shape: BoxShape.circle),
                    child: const Icon(Icons.favorite_border, size: 18, color: Colors.red),
                  ),
                ),
              ],
            ),
            Padding(
              padding: const EdgeInsets.all(12.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start, 
                children: [
                  Text(title, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16), maxLines: 1, overflow: TextOverflow.ellipsis),
                  const SizedBox(height: 4),
                  Row(
                    children: [
                      const Icon(Icons.location_on, size: 14, color: Colors.grey),
                      const SizedBox(width: 4),
                      Text(location, style: const TextStyle(color: Colors.grey, fontSize: 12)),
                    ],
                  ),
                  const SizedBox(height: 10),
                  Text(price, style: const TextStyle(fontWeight: FontWeight.bold, color: Color(0xFF1A237E), fontSize: 14)), 
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
