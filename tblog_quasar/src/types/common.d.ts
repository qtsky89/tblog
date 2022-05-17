declare module 't-common' {
  export interface Post {
    id: number
    title: string
    body: string
    description: string
    create_date: string
    tags: Array<string>
  }

  export interface IndexState {
    posts: Array<Post>
    tags: Array<string>
  }
}
