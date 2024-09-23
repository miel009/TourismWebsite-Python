# TourismWebsite-Python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>
    <h2> Sistema de Gestión de Destinos Turísticos </h2>
    <h2> 1. Objetivo </h2>
    <p> Este documento describe los requisitos del sistema para la migración y mejora del sistema de gestión de destinos turísticos de la agencia TravelEasy. El objetivo es proporcionar una plataforma más completa y accesible tanto para los usuarios finales como para los encargados de turismo y ventas, mejorando la experiencia de planificación y reserva mediante la personalización de itinerarios, la gestión integral de destinos y la implementación de recomendaciones automáticas.</p>
    <h2>2. Beneficios: </h2>
    <p>Para los usuarios finales: Simplifica la búsqueda y la reserva de viajes al proporcionar una plataforma integral 3 que ofrece información detallada y recomendaciones en cada destino. La plataforma ofrece desde destinos, paquetes, hasta servicios adicionales como traslados, facilitando así la toma de decisiones y mejorando la experiencia del usuario para la reserva final. 
        En el caso de que el usuario final prefiera un asesoramiento personalizado, deberá suscribirse. Se podrá llevar a cabo mediante el formulario de contacto (luego será llamado por el sector de ventas) o físicamente en la sede correspondiente, en el cual, el encargado de ventas brindará un asesoramiento particular para adecuarse a los requerimientos del usuario final/pasajero y realizar la reserva.
        Para la  empresa: optimiza la gestión y creación de destinos turísticos, agilizando las tareas diarias del encargado de turismo y el personal de ventas. Esto permite ofrecer una amplia variedad de opciones a los usuarios finales, mejorando la capacidad de la empresa para satisfacer sus necesidades y preferencias.
       </p>
    <h2>3.Alcance</h2> 
    <p> El sistema permitirá a los clientes finales buscar, comparar y reservar destinos turísticos, personalizando sus itinerarios y recibiendo recomendaciones basadas en sus preferencias. Además, ofrecerá a los encargados de turismos herramientas avanzadas para gestionar destinos y paquetes turísticos. Y a los encargados de ventas, proporcionar una interfaz intuitiva para el asesoramiento personalizado para los clientes finales. 
        La migración incluirá un rediseño completo de la interfaz de usuario, medidas de seguridad mejoradas y la expansión de la oferta de destinos a nivel global.
     </p>
    <h2>4.Referencias</h2>   
    <p> Este proyecto toma como referencia las funcionalidades avanzadas y mejores prácticas de las plataformas líderes en la industria: Klook, Travelport y Travel Leaders Group.
    </p>
    <h2>5. Limitaciones del sistema</h2>   
        El sistema solo estará disponible para dispositivos de escritorio (Windows 8 o superior).
        El sistema no está diseñado para ser utilizado en dispositivos móviles (smartphones o tablets)
        El acceso al sistema será únicamente a través de la agencia o plataforma para usuarios finales, pero no habrá acceso móvil en esta fase inicial.
    <h2>6.1 Módulo de Gestión de Destinos Turísticos</h2>
    <h3>6.1.1 Requisitos funcionales</h3> 
    <p> RF1.1: El encargado de turismo deberá autenticarse con credenciales de acceso.
        RF1.2: El encargado de turismo podrá agregar un nuevo destino, incluyendo información como país, región, rango de edad, actividades recomendadas, transporte disponible y temporada óptima.
        RF1.3: El sistema permitirá al encargado de turismo eliminar o modificar la información de destinos  y paquetes existentes.
        RF1.4: El encargado de turismo podrá crear paquetes turísticos, combinando diferentes actividades recreativas,tours, servicios de transporte y servicios adicionales.
        RF1.5: El sistema debe permitir la gestión global de destinos, ampliando el rango de Sudamérica a nivel internacional.
        RF1.6: Los encargados de turismo podrán ver una lista actualizada de destinos y paquetes turísticos.
        6.1.2 Requisitos no funcionales
        RNF1.1: El sistema debe garantizar tiempos de respuesta rápidos para la creación y actualización de destinos.
        RNF1.2: Se deberá restringir el acceso no autorizado.
        RNF1.3: La interfaz del sistema debe ser moderna, intuitiva y compatible con los estándares de usabilidad.
       </p> 
    <h2>6.2 Módulo de Ventas de Paquetes Turísticos </h2>
    <h3>6.2.1 Requisitos funcionales</h3>
    <p> RF2.1: El encargado de ventas deberá autenticarse con credenciales de acceso.
        RF2.2: El sistema debe permitir visualizar la lista de destinos disponibles.
        RF2.3: El encargado de ventas podrá filtrar los destinos por tipo de turismo y características del cliente (edad, preferencias).
        RF2.4: El encargado de ventas podrá agregar servicios adicionales como traslados o alquiler de autos, ajustados al paquete seleccionado por el cliente.
        RF2.5: El sistema debe generar reservas con comprobantes que incluyan los detalles del cliente, destinos seleccionados,transporte y servicios adicionales.
      </p>
    <h3>6.2.2 Requisitos no funcionales</h3>
    <p> RNF2.1: El sistema debe ofrecer tiempos de respuesta rápidos al seleccionar destinos o generar reservas.
        RNF2.2: La seguridad de las reservas debe garantizarse mediante el acceso restringido.
        RNF2.3: La interfaz de usuario debe ser fácil de usar, moderna y adaptada al flujo de trabajo del equipo de ventas.
       </p>
    <h2>6.3 Módulo del Usuario Final/Pasajero.</h2>
    <h3>6.3.1 Requisitos funcionales</h3>
    <p> RF3.1: Los clientes podrán buscar y comparar destinos turísticos, visualizar información detallada sobre cada uno y seleccionar aquellos que se ajusten a sus preferencias.
        RF3.2: El sistema permitirá a los usuarios finales crear itinerarios personalizados, combinando destinos, actividades, traslados y alojamiento.
        RF3.3: Los usuarios recibirán recomendaciones automáticas basadas en su historial de búsqueda y preferencias (eso será si se suscriben al plan premium)
        RF3.4: El sistema permitirá a los clientes finales gestionar sus reservas y recibir comprobantes con un código único.
   </p>
    <h3>6.3.2 Requisitos no funcionales</h3> 
        RNF3.1: El sistema debe garantizar tiempos de respuesta rápidos para la búsqueda y personalización de itinerarios.
        RNF3.2: La seguridad de la información de los usuarios finales estará garantizada mediante el acceso restringido.
        RNF3.3: La interfaz de usuario debe ser intuitiva, moderna y atractiva, alineada con las mejores prácticas de usabilidad para plataformas turísticas.
    <h2>6.4 Requisitos no funcionales globales</h2>
    <p> RNFG1: Compatibilidad con Windows 8, 10 o superior.
        RNFG2: Requiere al menos 4 GB de espacio en disco duro.
        RNFG3: Actualización constante para mantenerse alineado con las tendencias del mercado.
        RNFG4: La interfaz debe cumplir con estándares de usabilidad y diseño modernos, orientados también al usuario final.
        RNFG5: Debe incluir sistemas de autenticación.
        RNFG6:Tiempos de respuesta inferiores a 3 segundos para operaciones de búsqueda, creación de itinerarios y generación de reservas.
    </p>
    <h2> Diagrama de casos de uso.</h2>
    <img width="362" alt="image" src="https://github.com/user-attachments/assets/4143bc79-1a5b-4163-a59e-418e041acbcc">
    <h2> Diagrama de entidad relación.</h2>
    <img width="362" alt="image" src="https://github.com/user-attachments/assets/528e2606-51d6-49ba-bb06-d164d55e16fe">
    <h2>Diagrama de clases </h2>
    <img width="362" alt="image" src="https://github.com/user-attachments/assets/1f451362-4ea7-46c9-a46b-eb8b40e481cf">
</body>
</html>
