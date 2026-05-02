<center>

![./media/logo-upt.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERÍA**

**Escuela Profesional de Ingeniería de Sistemas**

**Proyecto Analizador Estático de Código con Métricas**

Curso: *Calidad y Pruebas de Software*

Docente: *Mag. Patrick Cuadros Quiroga*

Integrantes:

***Ramos Atahuachi, Fabricio Farid Edmilson (2023076798)***

***Colque Quispe, Rodrigo Sídney (2023077078)***

**Tacna – Perú**

***2026***

</center>

---

# Especificación de Requerimientos de Software (FD03)

## CONTROL DE VERSIONES
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1.0 | MPV | ELV | ARV | 15/01/2026 | Versión Original |

---

## 1. Introducción
El presente documento describe la Especificación de Requerimientos de Software para el proyecto de **Analizador Estático de Código**. Este sistema es una aplicación web diseñada para evaluar la calidad del código fuente mediante técnicas de análisis léxico, sintáctico y árboles de sintaxis abstracta (AST). Implementado con una arquitectura por capas y desplegado mediante contenedores, el sistema permite a los desarrolladores identificar vulnerabilidades, medir métricas de calidad y visualizar los resultados en un dashboard interactivo.

---

## 2. Generalidades de la Empresa

### 2.1. Nombre de la empresa
Analizador Estático de Código con Métricas

### 2.2. Visión
Ser la herramienta académica y profesional de referencia a nivel regional para el aseguramiento de la calidad del software, fomentando buenas prácticas de programación mediante el análisis automatizado.

### 2.3. Misión
Proveer a los desarrolladores e ingenieros de software un motor de análisis estático preciso y eficiente, capaz de medir métricas de código y detectar anomalías estructurales para reducir la deuda técnica en los proyectos.

### 2.4. Organigrama
<img width="1270" height="478" alt="image" src="https://github.com/user-attachments/assets/0e7733d0-158c-4487-9e1b-166b1c42fec2" />


---

## 3. Visionamiento del Proyecto

### 3.1. Descripción del Problema/Oportunidad
El equipo desarrolla una plataforma integral que permite a los usuarios someter fragmentos de código para que un motor interno deslose su estructura y devuelva métricas de calidad sin necesidad de ejecución.

### 3.2. Objetivos de Negocio
* Automatizar la revisión de código para reducir el tiempo en auditorías manuales.
* Proporcionar métricas claras sobre complejidad y estructuración.
* Mantener un registro histórico para evaluar la evolución del código.

### 3.3. Objetivos de Diseño
* Implementar una **Arquitectura Limpia (Clean Architecture)** separando Presentación, Negocios, Persistencia y Motor Core.
* Desarrollar un dashboard interactivo para visualización gráfica de métricas.
* Utilizar un sistema de rutas modularizado para autenticación y análisis.

### 3.4. Alcance del Proyecto
* Gestión de sesiones y autenticación.
* Procesamiento de código: Análisis Léxico, Sintáctico y generación de AST.
* Cálculo de métricas estáticas (complejidad, líneas de código, etc.).
* Almacenamiento de reportes generados.

---

## 4. Especificación de Requerimientos

### 4.1. Requerimientos Funcionales
| Código | Requerimiento Funcional | Descripción | Prioridad |
| :--- | :--- | :--- | :--- |
| RF01 | Autenticación de Usuarios | Login y registro mediante credenciales (auth_router). | Alta |
| RF02 | Ingreso de Código | Ingreso de código fuente vía web para evaluación. | Alta |
| RF03 | Análisis Léxico | Identificación de palabras clave, operadores y literales. | Alta |
| RF04 | Análisis Sintáctico y AST | Validación gramatical y construcción del árbol AST. | Alta |
| RF05 | Coordinación de Análisis | Orquestación de pasos y cálculo de métricas centralizado. | Alta |
| RF06 | Dashboard de Resultados | Vista de resumen con gráficas y errores (dashboard.html). | Media |
| RF07 | Historial de Análisis | Guardado de resultados vinculados al usuario. | Media |

### 4.2. Requerimientos No Funcionales
| Código | Requerimiento No Funcional | Descripción | Prioridad |
| :--- | :--- | :--- | :--- |
| RNF01 | Rendimiento | Análisis de <1000 líneas en menos de 3 segundos. | Alta |
| RNF02 | Despliegue | Orquestación mediante contenedores Docker. | Alta |
| RNF03 | Modularidad | Motor desacoplado de la base de datos para testeo. | Alta |
| RNF04 | Seguridad | Encriptación de contraseñas en repositorio de usuarios. | Alta |

---

## 5. Reglas de Negocio
1.  Solo usuarios autenticados acceden al dashboard y ejecutan análisis.
2.  El historial es privado; solo el propietario del código puede ver sus métricas.
3.  Si ocurre un error léxico, el motor debe detenerse antes de intentar generar el AST.

---

## 6. Fase de Desarrollo

### 6.1. Perfiles de Usuario
* **Desarrollador / Usuario Estándar**: Sube código, revisa reportes de calidad y consulta su historial de mejora técnica.

### 6.2. Modelo Conceptual 
#### 6.2.1 Diagrama de Paquetes
<img width="723" height="556" alt="image" src="https://github.com/user-attachments/assets/a06996fb-1a7f-4879-a944-cec7a3963dc7" />

#### 6.2.2 Casos de Uso
<img width="488" height="512" alt="image" src="https://github.com/user-attachments/assets/0daa46c5-e65c-4b11-9d77-171262ee8237" />

#### 6.2.3 Escenarios Casos de Uso

### 6.3. Modelo Lógico
#### 6.3.1 Análisis de Objetos
#####CU01: Realizar el Login
<img width="798" height="282" alt="image" src="https://github.com/user-attachments/assets/224da8ca-3766-4edb-b168-a25572377c7b" />

#####CU02: Someter Código a Análisis
<img width="822" height="433" alt="image" src="https://github.com/user-attachments/assets/7fe5bc27-aa17-49b7-91ac-476104c8d1d1" />

#####CU03: CU03: Visualizar Dashboard de Métricas
<img width="788" height="337" alt="image" src="https://github.com/user-attachments/assets/e571ad7a-05f6-4899-9d89-bded7a69345d" />

#####CU04: Consultar Historial de Análisis
<img width="801" height="374" alt="image" src="https://github.com/user-attachments/assets/623c9776-cd70-4bca-8185-04267d3a535d" />

#### 6.3.2 Diagrama de Actividades con objetos
#####CU01: Realizar el Login
<img width="329" height="604" alt="image" src="https://github.com/user-attachments/assets/8e27692a-b9fa-4a4f-b02f-2fce9196a345" />

#####CU02: Someter Código a Análisis
<img width="178" height="661" alt="image" src="https://github.com/user-attachments/assets/06a3e3b8-3aac-44fc-85d3-4ba65981b3e5" />

#####CU03: CU03: Visualizar Dashboard de Métricas
<img width="176" height="587" alt="image" src="https://github.com/user-attachments/assets/add5c384-e1a4-4f1c-abf7-6a50fae16878" />

#####CU04: Consultar Historial de Análisis
<img width="194" height="589" alt="image" src="https://github.com/user-attachments/assets/b5e4b20f-9283-4496-be68-2fbc31954fdb" />

#### 6.3.3 Diagrama de secuencia
#####CU01: Realizar el Login
<img width="1150" height="644" alt="image" src="https://github.com/user-attachments/assets/b797b64e-67b9-47f0-9770-97413e688335" />

#####CU02: Someter Código a Análisis
<img width="1388" height="630" alt="image" src="https://github.com/user-attachments/assets/31a49e4f-e5ce-4a60-b0d2-45789ddf850f" />

#####CU03: CU03: Visualizar Dashboard de Métricas
<img width="1249" height="653" alt="image" src="https://github.com/user-attachments/assets/7a8a8f89-58ce-4bd8-bec6-d42aec033e33" />

#####CU04: Consultar Historial de Análisis
<img width="1252" height="578" alt="image" src="https://github.com/user-attachments/assets/f3899d7c-d7a2-4c9a-a2c7-856a1461460a" />

---

## 7. Conclusiones y Recomendaciones

### 7.1. Conclusiones
* **Automatización**: Reduce drásticamente el tiempo de auditoría manual mediante el uso de AST.
* **Mantenibilidad**: La arquitectura limpia garantiza que los cambios en la UI o BD no afecten la lógica del motor.
* **Valor Educativo**: El feedback visual inmediato ayuda a los desarrolladores a escribir código más limpio.

### 7.2. Recomendaciones
* **Integración CI/CD**: Automatizar el análisis en cada "commit" o "pull request" vía Docker.
* **Polimorfismo Gramatical**: Ampliar el soporte a lenguajes como JavaScript o C# cargando reglas dinámicas.
* **Sugerencias de Refactorización**: Evolucionar el motor para detectar "code smells" y proponer mejoras automáticas.

---
