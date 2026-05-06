# 🐛 Challenge Débogage : Publisher Silencieux

Ce dépôt contient la version corrigée d'un publisher ROS 2 qui ne parvenait pas à diffuser ses données.

## 🛠 Bugs Identifiés et Corrigés
1.  **Namespace (Topic)** : Ajout du `/` devant `robot/status` pour garantir que le topic soit accessible globalement et non relatif à un namespace local non défini.
2.  **Instanciation** : Remplacement de `msg = String` par `msg = String()` (Appel du constructeur). Sans les parenthèses, on manipule la classe et non un objet.
3.  **Appel de fonction** : La méthode `publish()` nécessitait l'argument `msg` pour savoir quelle donnée envoyer.

## 🚀 Installation & Test
```bash
cd ~/ros2_ws
colcon build --packages-select publisher_silencieux
source install/setup.bash

# Lancer le node
ros2 launch publisher_silencieux status_launch.py
```

## 📊 Vérification
Dans un autre terminal :
```bash
ros2 topic echo /robot/status
```

---
**Développeur :** Maria Lagab  
**Spécialité :** Robotique et Système Intelligent
