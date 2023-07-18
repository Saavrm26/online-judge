export interface Filter {
  difficulty: Array<string>;
  tags: Array<string>;
}

export interface problem {
  name: string;
  statement?: string;
  difficulty: string;
  tags: Array<string>;
}

