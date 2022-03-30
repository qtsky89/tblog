// vetur.config.js ( https://vuejs.github.io/vetur/reference/#example )
/** @type {import('vls').VeturConfig} */
module.exports = {
  settings: {
    'vetur.useWorkspaceDependencies': false,
    'vetur.experimental.templateInterpolationService': false,
  },
  projects: [
    {
      root: './tblog_vue/',
      package: './package.json',
      tsconfig: './tsconfig.json',
      globalComponents: ['./components/**/*.vue'],
    },
  ],
}
