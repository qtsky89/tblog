declare module 't-common' {
  export interface Post {
    id: number | null
    title: string
    body: string
    description: string
    created_date: string
    tags: Array<string>
  }

  export interface IndexState {
    posts: Array<Post>
    tags: Array<string>
    selectedTag: string
  }

  export interface UserState {
    user: User
  }
  export interface User {
    email: string
    isSu: boolean
    picture: string
    encodedJwt: string
  }
}
