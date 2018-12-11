+++
title = "{{cookiecutter.api_version}}"
description = ""
+++

<div id="swagger-ui"></div>
<link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@3.12.1/swagger-ui.css">

<script src="https://unpkg.com/swagger-ui-dist@3.12.1/swagger-ui-standalone-preset.js"></script>
<script src="https://unpkg.com/swagger-ui-dist@3.12.1/swagger-ui-bundle.js"></script>

<script>
    // .swagger-ui .info hgroup.main 
    window.onload = function () {
        // Build a system
        const ui = SwaggerUIBundle({
            url: "../{{cookiecutter.api_version}}_{{cookiecutter.project_name.lower()}}.swagger.json",

            // https://github.com/swagger-api/swagger-ui/blob/master/docs/usage/configuration.md
            dom_id: '#swagger-ui',
            deepLinking: true,
            displayOperationId: true,
            defaultModelsExpandDepth: 0,
            defaultModelExpandDepth: 100,
            defaultModelRendering: "model",
            supportedSubmitMethods: [],
            presets: [
                SwaggerUIBundle.presets.apis,
                // SwaggerUIStandalonePreset
            ],
            plugins: [
                SwaggerUIBundle.plugins.DownloadUrl
            ],
            layout: "BaseLayout",
        })
        window.ui = ui
    }
</script>
