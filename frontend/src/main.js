import { createApp } from 'vue'
import router from './router'
import App from './App.vue'

import './css/style.css'

// Components
import Spinner from './components/Spinner.vue'

const app = createApp(App)

// Components registry
app.component('Spinner', Spinner)

app.use(router)
app.mount('#app')

