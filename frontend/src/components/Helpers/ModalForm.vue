<!-- components/BaseFormModal.vue -->
<template>
    <transition name="fade">
      <div v-if="visible" class="fixed inset-0 z-50 flex items-center justify-center backdrop-blur-sm bg-black/20">
        <div class="bg-white dark:bg-gray-900 rounded-2xl shadow-2xl w-full max-w-lg p-6 animate-fade-in">
  
          <h2 class="text-xs sm:text-2xl font-bold text-gray-800 dark:text-white mb-6">
            {{ title }}
          </h2>
  
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div class="block" v-for="field in fields" :key="field.model">
              <span class="text-xs">{{ field.label }}</span>
              <input
                v-model="form[field.model]"
                :type="field.type || 'text'"
                :placeholder="field.placeholder || field.label"
                :disabled="field.disabled"
                class="text-xs w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-600 dark:bg-gray-800 dark:text-white disabled:bg-slate-200 dark:disabled:bg-gray-600"
              />
            </div>
            <slot name="add-input" :field="field" :form="form"></slot>
          </div>
  
          <div class="mt-6 flex justify-end space-x-4">
            <button @click="onCancel"
              class="cursor-pointer text-xs mx-2 px-4 py-2 rounded-lg bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:text-white">
              Cancel
            </button>
            <button @click="onSubmit"
              class="cursor-pointer text-xs px-4 py-2 rounded-lg text-white"
              :class="submitClass">
              {{ submitText }}
            </button>
          </div>
  
        </div>
      </div>
    </transition>
  </template>
  
  <script setup>
  import { reactive, watch } from 'vue'
  import { cloneDeep } from 'lodash-es'
  
  const props = defineProps({
    visible: Boolean,
    title: { type: String, default: 'Form' },
    modelValue: { type: Object, default: () => ({}) },
    fields: { type: Array, required: true },
    submitText: { type: String, default: 'Submit' },
    submitClass: { type: String, default: 'bg-slate-600 hover:bg-slate-700' }
  })
  
  const emit = defineEmits(['update:visible', 'submit'])
  
  const form = reactive(cloneDeep(props.modelValue))
  
  watch(() => props.modelValue, (val) => {
    Object.assign(form, cloneDeep(val))
  })
  
  const onCancel = () => {
    emit('update:visible', false)
  }
  
  const onSubmit = () => {
    emit('submit', form)
    emit('update:visible', false)
  }
  </script>
  