allprojects {
    repositories {
        google()
        mavenCentral()
    }
}

// Fix pour l'erreur "different roots" entre le disque C: et D:
val rootBuildDir = rootProject.layout.projectDirectory.dir("../build")
rootProject.layout.buildDirectory.set(rootBuildDir)

subprojects {
    val subprojectDir = project.projectDir.absolutePath
    val rootDir = rootProject.projectDir.absolutePath

    // Si le sous-projet est sur le même disque que le projet racine (ex: D:), on redirige le buildDir
    // vers le dossier build à la racine du projet Flutter (D:\...\build)
    if (subprojectDir.take(1).equals(rootDir.take(1), ignoreCase = true)) {
        project.layout.buildDirectory.set(rootBuildDir.dir(project.name))
    }
}

// Désactivation des tests unitaires pour les plugins (évite l'erreur de disque et accélère le build)
subprojects {
    afterEvaluate {
        if (project.name != "app") {
            tasks.forEach { task ->
                if (task.name.contains("UnitTest")) {
                    task.enabled = false
                }
            }
        }
    }
}

subprojects {
    project.evaluationDependsOn(":app")
}

tasks.register<Delete>("clean") {
    delete(rootProject.layout.buildDirectory)
}
