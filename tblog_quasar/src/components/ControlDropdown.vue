<template>
  <div>
    <!-- TODO: add control feature (create, update, delete, login, logout)-->
    <q-btn-dropdown class="q-btn--flat">
      <template #label>
        <q-avatar>
          <img
            class="bg-black"
            src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg"
          />
        </q-avatar>
      </template>

      <q-list>
        <q-item clickable v-close-popup to="/create">
          <q-item-section avatar>
            <q-avatar
              size="25px"
              icon="add"
              color="blue-10"
              text-color="white"
            />
          </q-item-section>
          <q-item-section>
            <q-item-label>Create</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-close-popup to="/update">
          <q-item-section avatar>
            <q-avatar
              size="25px"
              icon="edit"
              color="green-10"
              text-color="white"
            />
          </q-item-section>
          <q-item-section>
            <q-item-label>Update</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>

      <q-item clickable v-close-popup to="/delete">
        <q-item-section avatar>
          <q-avatar size="25px" icon="add" color="red-10" text-color="white" />
        </q-item-section>
        <q-item-section>
          <q-item-label>Delete</q-item-label>
        </q-item-section>
      </q-item>
    </q-btn-dropdown>
  </div>
</template>
