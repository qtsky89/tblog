export interface Todo {
  id: number
  content: string
}

export interface Meta {
  totalCount: number
}

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
